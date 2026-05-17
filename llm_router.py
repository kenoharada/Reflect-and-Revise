from dataclasses import dataclass
from typing import Any, TypedDict
import random
import requests
import json
import os
import hashlib
import dotenv
import time
import aiohttp
import asyncio

dotenv.load_dotenv()

OPENROUTER_USER_MAX_LEN = 128


def _normalize_openrouter_user(config: dict[str, Any] | None) -> dict[str, Any]:
    normalized = dict(config or {})
    user_value = normalized.get("user")
    if isinstance(user_value, str) and len(user_value) > OPENROUTER_USER_MAX_LEN:
        suffix = hashlib.sha1(user_value.encode("utf-8")).hexdigest()[:12]
        prefix_len = OPENROUTER_USER_MAX_LEN - len(suffix) - 1
        normalized["user"] = f"{user_value[:prefix_len]}_{suffix}"
    return normalized

def get_llm_response(messages, model_name, config, verbose: bool = False, timeout: int = 60, max_retries: int = 3, retry_delay: float = 1.0):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer " + os.getenv("OPENROUTER_API_KEY"),
        "Content-Type": "application/json",
    }
    config = _normalize_openrouter_user(config)
    payload = {
        "model": model_name,
        "messages": messages,
        **(config or {}),
    }

    last_exception = None
    for attempt in range(max_retries + 1):
        try:
            response = requests.post(
                url=url,
                headers=headers,
                data=json.dumps(payload),
                timeout=timeout,
            )
            if response.status_code >= 400:
                error_msg = f"OpenRouter error {response.status_code}: {response.text}"
                text = response.text
                print(f"Error response: {text}")
                if verbose:
                    print("Request payload:")
                    print(json.dumps(payload, ensure_ascii=False, indent=2))
                print(error_msg)
                if response.status_code in [429, 500, 502, 503, 504] and attempt < max_retries:
                    sleep_s = retry_delay * (2 ** attempt)
                    print(f"Attempt {attempt + 1} failed with status {response.status_code}, retrying in {sleep_s}s...")
                    time.sleep(sleep_s)
                    continue
                response.raise_for_status()
            data = response.json()
            if verbose:
                print(json.dumps(data, indent=2, ensure_ascii=False))
            return data.get("choices", [{}])[0].get("message", {}).get("content", "")
        except (requests.RequestException, requests.Timeout) as e:
            last_exception = e
            if attempt < max_retries:
                sleep_s = retry_delay * (2 ** attempt)
                print(f"Attempt {attempt + 1} failed with {type(e).__name__}: {e}, retrying in {sleep_s}s...")
                time.sleep(sleep_s)
                continue
            raise RuntimeError(f"Max retries ({max_retries}) exceeded. Last error: {e}") from e

    if last_exception:
        raise RuntimeError(f"Max retries exceeded. Last error: {last_exception}")
    return ""


async def get_llm_response_async(messages, model_name, config, session: "aiohttp.ClientSession | None" = None, timeout: int = 90, max_retries: int = 5, retry_delay: float = 1.0, concurrency: int | None = None):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer " + os.getenv("OPENROUTER_API_KEY", ""),
        "Content-Type": "application/json",
    }
    config = _normalize_openrouter_user(config)
    payload = {
        "model": model_name,
        "messages": messages,
        **(config or {}),
    }

    owns_session = session is None
    if owns_session:
        connector = None
        if concurrency is not None:
            connector = aiohttp.TCPConnector(limit=concurrency, limit_per_host=concurrency)
        session = aiohttp.ClientSession(connector=connector)
    
    last_exception = None
    try:
        for attempt in range(max_retries + 1):
            try:
                async with session.post(url, headers=headers, json=payload, timeout=timeout) as resp:
                    if resp.status >= 400:
                        text = await resp.text()
                        error_msg = f"OpenRouter error {resp.status}: {text}"
                        if resp.status in [429, 500, 502, 503, 504] and attempt < max_retries:
                            sleep_s = retry_delay * (2 ** attempt)
                            print(f"Attempt {attempt + 1} failed with status {resp.status}, retrying in {sleep_s}s...")
                            await asyncio.sleep(sleep_s)
                            continue
                        raise RuntimeError(error_msg)
                    data = await resp.json()
                    return data.get("choices", [{}])[0].get("message", {}).get("content", "")
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                last_exception = e
                if attempt < max_retries:
                    sleep_s = retry_delay * (2 ** attempt)
                    print(f"Attempt {attempt + 1} failed with {type(e).__name__}: {e}, retrying in {sleep_s}s...")
                    await asyncio.sleep(sleep_s)
                    continue
                raise RuntimeError(f"Max retries ({max_retries}) exceeded. Last error: {e}")
        
        if last_exception:
            raise RuntimeError(f"Max retries exceeded. Last error: {last_exception}")
    finally:
        if owns_session:
            await session.close()


async def get_llm_responses_batch_async(messages_list, model_name, config, session: "aiohttp.ClientSession | None" = None, timeout: int = 90, max_retries: int = 3, retry_delay: float = 1.0, concurrency: int | None = None):
    owns_session = session is None
    if owns_session:
        connector = None
        if concurrency is not None:
            connector = aiohttp.TCPConnector(limit=concurrency, limit_per_host=concurrency)
        session = aiohttp.ClientSession(connector=connector)
    try:
        sem = asyncio.Semaphore(concurrency) if concurrency is not None else None

        async def run_one(messages):
            if sem is None:
                return await get_llm_response_async(
                    messages=messages,
                    model_name=model_name,
                    config=config,
                    session=session,
                    timeout=timeout,
                    max_retries=max_retries,
                    retry_delay=retry_delay
                )
            async with sem:
                return await get_llm_response_async(
                    messages=messages,
                    model_name=model_name,
                    config=config,
                    session=session,
                    timeout=timeout,
                    max_retries=max_retries,
                    retry_delay=retry_delay
                )
        tasks = []
        for messages in messages_list:
            tasks.append(asyncio.create_task(run_one(messages)))
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results
    finally:
        if owns_session:
            await session.close()

