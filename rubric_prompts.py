SIMPLEST_ETS_RUBRIC = 'Based on the response\'s content, rate the response on a scale of 1 to 5.'

SIMPLE_ETS_RUBRIC = '''\
Score 5: Fully addresses the topic with clear organization, strong examples, smooth flow, and excellent language use.
Score 4: Addresses the topic well, with good organization and examples, though some points could be clearer.
Score 3: Covers the topic but lacks depth or clarity, with limited language variety and occasional errors.
Score 2: Weak response with poor organization, insufficient examples, and frequent language errors.
Score 1: Very weak, disorganized, or off-topic with serious language issues.'''


ETS_RUBRIC_FOR_3 = '''## Score 3 
An essay at this level largely accomplishes all of the following:
- addresses the topic and task well, though some points may not be fully elaborated
- is generally well organized and well developed, using appropriate and sufficient explanations, exemplifications, and/or details
- displays unity, progression, and coherence, though it may contain occasional redundancy, digression, or unclear connections
- displays facility in the use of language, demonstrating syntactic variety and range of vocabulary, though it will probably have occasional noticeable minor errors in structure, word form, or use of idiomatic language that do not interfere with meaning

## Score 2
An essay at this level is marked by one or more of the following:
- addresses the topic and task using somewhat developed explanations, exemplifications, and/or details
- displays unity, progression, and coherence, though connection of ideas may be occasionally obscured
- may demonstrate inconsistent facility in sentence formation and word choice that may result in lack of clarity and occasionally obscure meaning
- may display accurate but limited range of syntactic structures and vocabulary

## Score 1
An essay at this level may reveal one or more of the following weaknesses:
- limited development in response to the topic and task
- inadequate organization or connection of ideas
- inappropriate or insufficient exemplifications, explanations, or details to support or illustrate generalizations in response to the task
- a noticeably inappropriate choice of words or word forms
- an accumulation of errors in sentence structure and/or usage'''


ETS_RUBRIC = '''## Score 5
An essay at this level largely accomplishes all of the following:
- effectively addresses the topic and task
- is well organized and well developed, using clearly appropriate explanations, exemplifications, and/or details
- displays unity, progression, and coherence
- displays consistent facility in the use of language, demonstrating syntactic variety, appropriate word choice, and idiomaticity, though it may have minor lexical or grammatical errors

## Score 4 
An essay at this level largely accomplishes all of the following:
- addresses the topic and task well, though some points may not be fully elaborated
- is generally well organized and well developed, using appropriate and sufficient explanations, exemplifications, and/or details
- displays unity, progression, and coherence, though it may contain occasional redundancy, digression, or unclear connections
- displays facility in the use of language, demonstrating syntactic variety and range of vocabulary, though it will probably have occasional noticeable minor errors in structure, word form, or use of idiomatic language that do not interfere with meaning

## Score 3
An essay at this level is marked by one or more of the following:
- addresses the topic and task using somewhat developed explanations, exemplifications, and/or details
- displays unity, progression, and coherence, though connection of ideas may be occasionally obscured
- may demonstrate inconsistent facility in sentence formation and word choice that may result in lack of clarity and occasionally obscure meaning
- may display accurate but limited range of syntactic structures and vocabulary

## Score 2
An essay at this level may reveal one or more of the following weaknesses:
- limited development in response to the topic and task
- inadequate organization or connection of ideas
- inappropriate or insufficient exemplifications, explanations, or details to support or illustrate generalizations in response to the task
- a noticeably inappropriate choice of words or word forms
- an accumulation of errors in sentence structure and/or usage

## Score 1
An essay at this level is seriously flawed by one or more of the following weaknesses:
- serious disorganization or underdevelopment
- little or no detail, or irrelevant specifics, or questionable responsiveness to the task
- serious and frequent errors in sentence structure or usage'''


NOTE_ASAP_1 = '''I have made an effort to remove personally identifying information from the essays using the Named Entity Recognizer (NER). The relevant entities are identified in the text and then replaced with a string such as "PERSON", "ORGANIZATION", "LOCATION", "DATE", "TIME", "MONEY", "PERCENT", "CAPS" (any capitalized word) and "NUM" (any digits). Please do not penalize the essay because of the anonymizations.'''

SIMPLEST_ASAP_RUBRIC_1 = 'Based on the response\'s content, rate the response on a scale of 1 to 6.'

SIMPLE_ASAP_RUBRIC_1 = '''\
Score Point 1: An undeveloped response that may take a position but offers no more than very minimal support.
Score Point 2: An under-developed response that may or may not take a position.
Score Point 3: A minimally-developed response that may take a position, but with inadequate support and details.
Score Point 4: A somewhat-developed response that takes a position and provides adequate support.
Score Point 5: A developed response that takes a clear position and provides reasonably persuasive support.
Score Point 6: A well-developed response that takes a clear and thoughtful position and provides persuasive support.'''

ASAP_RUBRIC_1 = f'''Score Point 1: An undeveloped response that may take a position but offers no more than very minimal support. Typical elements:
- Contains few or vague details.
- Is awkward and fragmented.
- May be difficult to read and understand.
- May show no awareness of audience.

Score Point 2: An under-developed response that may or may not take a position. Typical elements:
- Contains only general reasons with unelaborated and/or list-like details.
- Shows little or no evidence of organization.
- May be awkward and confused or simplistic.
- May show little awareness of audience.

Score Point 3: A minimally-developed response that may take a position, but with inadequate support and details. Typical elements:
- Has reasons with minimal elaboration and more general than specific details.
- Shows some organization.
- May be awkward in parts with few transitions.
- Shows some awareness of audience.

Score Point 4: A somewhat-developed response that takes a position and provides adequate support. Typical elements:
- Has adequately elaborated reasons with a mix of general and specific details.
- Shows satisfactory organization.
- May be somewhat fluent with some transitional language.
- Shows adequate awareness of audience.

Score Point 5: A developed response that takes a clear position and provides reasonably persuasive support. Typical elements:
- Has moderately well elaborated reasons with mostly specific details.
- Exhibits generally strong organization.
- May be moderately fluent with transitional language throughout.
- May show a consistent awareness of audience.

Score Point 6: A well-developed response that takes a clear and thoughtful position and provides persuasive support. Typical elements:
- Has fully elaborated reasons with specific details.
- Exhibits strong organization.
- Is fluent and uses sophisticated transitional language.
- May show a heightened awareness of audience.

Note: 
{NOTE_ASAP_1}'''


ASAP_RUBRIC_2 = '''Score Point 6: A Score Point 6 paper is rare. It fully accomplishes the task in a thorough and insightful manner and has a distinctive quality that sets it apart as an outstanding performance.
Ideas and Content
Does the writing sample fully accomplish the task (e.g., support an opinion, summarize, tell a story, or write an article)? Does it
- present a unifying theme or main idea without going off on tangents?
- stay completely focused on topic and task?
Does the writing sample include thorough, relevant, and complete ideas? Does it
- include in-depth information and exceptional supporting details that are fully developed?
- fully explore many facets of the topic?
Organization
Are the ideas in the writing sample organized logically? Does the writing
- present a meaningful, cohesive whole with a beginning, a middle, and an end (i.e., include an inviting introduction and a strong conclusion)?
- progress in an order that enhances meaning?
- include smooth transitions between ideas, sentences, and paragraphs to enhance meaning of text (i.e., have a clear connection of ideas and use topic sentences)?
Style
Does the writing sample exhibit exceptional word usage? Does it
- include vocabulary to make explanations detailed and precise, descriptions rich, and actions clear and vivid (e.g., varied word choices, action words, appropriate modifiers, sensory details)?
- demonstrate control of a challenging vocabulary?
Does the writing sample demonstrate exceptional writing technique?
- Is the writing exceptionally fluent?
- Does it include varied sentence patterns, including complex sentences?
- Does it demonstrate use of writer’s techniques (e.g., literary conventions such as imagery and dialogue and/or literary genres such as humor and suspense)?
Voice
Does the writing sample demonstrate effective adjustment of language and tone to task and reader? Does it
- exhibit appropriate register (e.g., formal, personal, or dialect) to suit task?
- demonstrate a strong sense of audience?
- exhibit an original perspective (e.g., authoritative, lively, and/or exciting)?
Score Point 5: A Score Point 5 paper represents a solid performance. It fully accomplishes the task, but lacks the overall level of sophistication and consistency of a Score Point 6 paper.
Ideas and Content
Does the writing sample fully accomplish the task (e.g., support an opinion, summarize, tell a story, or write an article)? Does it
- present a unifying theme or main idea without going off on tangents?
- stay focused on topic and task?
Does the writing sample include many relevant ideas? Does it
- provide in-depth information and more than adequate supporting details that are developed?
- explore many facets of the topic?
Organization
Are the ideas in the writing sample organized logically? Does the writing
- present a meaningful, cohesive whole with a beginning, a middle, and an end (i.e., include a solid introduction and conclusion)?
- progress in an order that enhances meaning of text?
- include smooth transitions (e.g., use topic sentences) between sentences and paragraphs to enhance meaning of text? (Writing may have an occasional lapse.)
Style
Does the writing sample exhibit very good word usage? Does it
- include vocabulary to make explanations detailed and precise, descriptions rich, and actions clear and vivid?
- demonstrate control of vocabulary?
Does the writing sample demonstrate very good writing technique?
- Is the writing very fluent?
- Does it include varied sentence patterns, including complex sentences?
- Does it demonstrate use of writer’s techniques (e.g., literary conventions such as imagery and dialogue and/or literary genres such as humor and suspense)?
Voice
Does the writing sample demonstrate effective adjustment of language and tone to task and reader? Does it
- exhibit appropriate register (e.g., formal, personal, or dialect) to suit task?
- demonstrate a sense of audience?
- exhibit an original perspective (e.g., authoritative, lively, and/or exciting)?
Score Point 4: A Score Point 4 paper represents a good performance. It accomplishes the task, but generally needs to exhibit more development, better organization, or a more sophisticated writing style to receive a higher score.
Ideas and Content
Does the writing sample accomplish the task (e.g., support an opinion, summarize, tell a story, or write an article)? Does it
- present a unifying theme or main idea? (Writing may include minor tangents.)
- stay mostly focused on topic and task?
Does the writing sample include relevant ideas? Does it
- include sufficient information and supporting details? (Details may not be fully developed; ideas may be listed.)
- explore some facets of the topic?
Organization
Are the ideas in the writing sample organized logically? Does the writing
- present a meaningful whole with a beginning, a middle, and an end despite an occasional lapse (e.g., a weak introduction or conclusion)?
- generally progress in an order that enhances meaning of text?
- include transitions between sentences and paragraphs to enhance meaning of text? (Transitions may be rough, although some topic sentences are included.)
Style
Does the writing sample exhibit good word usage? Does it
- include vocabulary that is appropriately chosen, with words that clearly convey the writer’s meaning?
- demonstrate control of basic vocabulary?
Does the writing sample demonstrate good writing technique?
- Is the writing fluent?
- Does it exhibit some varied sentence patterns, including some complex sentences?
- Does it demonstrate an attempt to use writer’s techniques (e.g., literary conventions such as imagery and dialogue and/or literary genres such as humor and suspense)?
Voice
Does the writing sample demonstrate an attempt to adjust language and tone to task and reader? Does it
- generally exhibit appropriate register (e.g., formal, personal, or dialect) to suit task? (The writing may occasionally slip out of register.)
- demonstrate some sense of audience?
- attempt an original perspective?
Score Point 3: A Score Point 3 paper represents a performance that minimally accomplishes the task. Some elements of development, organization, and writing style are weak.
Ideas and Content
Does the writing sample minimally accomplish the task (e.g., support an opinion, summarize, tell a story, or write an article)? Does it
- attempt a unifying theme or main idea?
- stay somewhat focused on topic and task?
Does the writing sample include some relevant ideas? Does it
- include some information with only a few details, or list ideas without supporting details?
- explore some facets of the topic?
Organization
Is there an attempt to logically organize ideas in the writing sample? Does the writing
- have a beginning, a middle, or an end that may be weak or absent?
- demonstrate an attempt to progress in an order that enhances meaning? (Progression of text may sometimes be unclear or out of order.)
- demonstrate an attempt to include transitions? (Are some topic sentences used? Are transitions between sentences and paragraphs weak or absent?)
Style
Does the writing sample exhibit ordinary word usage? Does it
- contain basic vocabulary, with words that are predictable and common?
- demonstrate some control of vocabulary?
Does the writing sample demonstrate average writing technique?
- Is the writing generally fluent?
- Does it contain mostly simple sentences (although there may be an attempt at more varied sentence patterns)?
- Is it generally ordinary and predictable?
Voice
Does the writing sample demonstrate an attempt to adjust language and tone to task and reader? Does it
- demonstrate a difficulty in establishing a register (e.g., formal, personal, or dialect)?
- demonstrate little sense of audience?
- generally lack an original perspective?
Score Point 2: A Score Point 2 paper represents a performance that only partially accomplishes the task. Some responses may exhibit difficulty maintaining a focus. Others may be too brief to provide sufficient development of the topic or evidence of adequate organizational or writing style.
Ideas and Content
Does the writing sample only partially accomplish the task (e.g., support an opinion, summarize, tell a story, or write an article)? Does it
- attempt a main idea?
- sometimes lose focus or ineffectively display focus?
Does the writing sample include few relevant ideas? Does it
- include little information and few or no details?
- explore only one or two facets of the topic?
Organization
Is there a minimal attempt to logically organize ideas in the writing sample?
- Does the writing have only one or two of the three elements: beginning, middle, and end?
- Is the writing sometimes difficult to follow? (Progression of text may be confusing or unclear.)
- Are transitions weak or absent (e.g., few or no topic sentences)?
Style
Does the writing sample exhibit minimal word usage? Does it
- contain limited vocabulary? (Some words may be used incorrectly.)
- demonstrate minimal control of vocabulary?
Does the writing sample demonstrate minimal writing technique?
- Does the writing exhibit some fluency?
- Does it rely mostly on simple sentences?
- Is it often repetitive, predictable, or dull?
Voice
Does the writing sample demonstrate language and tone that may be inappropriate to task and reader? Does it
- demonstrate use of a register inappropriate to the task (e.g., slang or dialect in a formal setting)?
- demonstrate little or no sense of audience?
- lack an original perspective?
Score Point 1: A Score Point 1 paper represents a performance that fails to accomplish the task. It exhibits considerable difficulty in areas of development, organization, and writing style. The writing is generally either very brief or rambling and repetitive, sometimes resulting in a response that may be difficult to read or comprehend.
Ideas and Content
Does the writing sample fail to accomplish the task (e.g., support an opinion, summarize, tell a story, or write an article)? Is it
- difficult for the reader to discern the main idea?
- too brief or too repetitive to establish or maintain a focus?
Does the writing sample include very few relevant ideas?
- Does it include little information with few or no details or unrelated details?
- Is it unsuccessful in attempts to explore any facets of the prompt?
Organization
Are the ideas in the writing sample organized illogically?
- Does it have only one or two of the three elements: beginning, middle, or end?
- Is it difficult to follow, with the order possibly difficult to discern?
- Are transitions weak or absent (e.g., without topic sentences)?
Style
Does the writing sample exhibit less than minimal word usage? Does it
- contain limited vocabulary, with many words used incorrectly?
- demonstrate minimal or less than minimal control of vocabulary?
Does the writing sample demonstrate less than minimal writing technique? Does it
- lack fluency?
- demonstrate problems with sentence patterns?
- consist of writing that is flat and lifeless?
Voice
Does the writing sample demonstrate language and tone that may be inappropriate to task and reader? Does it
- demonstrate difficulty in choosing an appropriate register?
- demonstrate a lack of a sense of audience?
- lack an original perspective?
'''

SIMPLE_ASAP_RUBRIC_2 = '''\
Score Point 6: A Score Point 6 paper is rare. It fully accomplishes the task in a thorough and insightful manner and has a distinctive quality that sets it apart as an outstanding performance.
Score Point 5: A Score Point 5 paper represents a solid performance. It fully accomplishes the task, but lacks the overall level of sophistication and consistency of a Score Point 6 paper.
Score Point 4: A Score Point 4 paper represents a good performance. It accomplishes the task, but generally needs to exhibit more development, better organization, or a more sophisticated writing style to receive a higher score.
Score Point 3: A Score Point 3 paper represents a performance that minimally accomplishes the task. Some elements of development, organization, and writing style are weak.
Score Point 2: A Score Point 2 paper represents a performance that only partially accomplishes the task. Some responses may exhibit difficulty maintaining a focus. Others may be too brief to provide sufficient development of the topic or evidence of adequate organizational or writing style.
Score Point 1: A Score Point 1 paper represents a performance that fails to accomplish the task. It exhibits considerable difficulty in areas of development, organization, and writing style. The writing is generally either very brief or rambling and repetitive, sometimes resulting in a response that may be difficult to read or comprehend.'''

ASAP_RUBRIC_3 = '''Score 3: The response demonstrates an understanding of the complexities of the text.
- Addresses the demands of the question
- Uses expressed and implied information from the text
- Clarifies and extends understanding beyond the literal
Score 2: The response demonstrates a partial or literal understanding of the text.
- Addresses the demands of the question, although may not develop all parts equally
- Uses some expressed or implied information from the text to demonstrate understanding
- May not fully connect the support to a conclusion or assertion made about the text(s)
Score 1: The response shows evidence of a minimal understanding of the text.
- May show evidence that some meaning has been derived from the text
- May indicate a misreading of the text or the question
- May lack information or explanation to support an understanding of the text in relation to the question
Score 0: The response is completely irrelevant or incorrect, or there is no response.'''


SIMPLEST_ASAP_RUBRIC_3 = 'Based on the response\'s content, rate the response on a scale of 0 to 3.'

SIMPLE_ASAP_RUBRIC_3 = '''\
Score 3: The response demonstrates an understanding of the complexities of the text.
Score 2: The response demonstrates a partial or literal understanding of the text.
Score 1: The response shows evidence of a minimal understanding of the text.
Score 0: The response is completely irrelevant or incorrect, or there is no response.'''


ASAP_RUBRIC_5 = '''Score Point 4: The response is a clear, complete, and accurate description of the mood created by the author. The response includes relevant and specific information from the memoir.
 
Score Point 3: The response is a mostly clear, complete, and accurate description of the mood created by the author. The response includes relevant but often general information from the memoir.
 
Score Point 2: The response is a partial description of the mood created by the author. The response includes limited information from the memoir and may include misinterpretations.
 
Score Point 1: The response is a minimal description of the mood created by the author. The response includes little or no information from the memoir and may include misinterpretations. 
OR 
The response relates minimally to the task.

Score Point 0: The response is incorrect or irrelevant or contains insufficient information to demonstrate comprehension.'''


SIMPLEST_ASAP_RUBRIC_5 = 'Based on the response\'s content, rate the response on a scale of 0 to 4.'


ASAP_RUBRIC_6 = '''Score Point 4: The response is a clear, complete, and accurate description of the obstacles the builders of the Empire State Building faced in attempting to allow dirigibles to dock there. The response includes relevant and specific information from the excerpt.
 
Score Point 3: The response is a mostly clear, complete, and accurate description of the obstacles the builders of the Empire State Building faced in attempting to allow dirigibles to dock there. The response includes relevant but often general information from the excerpt.
 
Score Point 2: The response is a partial description of the obstacles the builders of the Empire State Building faced in attempting to allow dirigibles to dock there. The response includes limited information from the excerpt and may include misinterpretations.
 
Score Point 1: The response is a minimal description of the obstacles the builders of the Empire State Building faced in attempting to allow dirigibles to dock there. The response includes little or no information from the excerpt and may include misinterpretations. 
OR 
The response relates minimally to the task.
 
Score Point 0: The response is totally incorrect or irrelevant, or contains insufficient evidence to demonstrate comprehension.'''


ASAP_RUBRIC_7 = '''A rating of 0-3 on the following four traits:
Ideas (points doubled)
Score 3: Tells a story with ideas that are clearly focused on the topic and are thoroughly developed with specific, relevant details.
Score 2: Tells a story with ideas that are somewhat focused on the topic and are developed with a mix of specific and/or general details.
Score 1: Tells a story with ideas that are minimally focused on the topic and developed with limited and/or general details.
Score 0: Ideas are not focused on the task and/or are undeveloped.
Organization
Score 3: Organization and connections between ideas and/or events are clear and logically sequenced. 
Score 2: Organization and connections between ideas and/or events are logically sequenced.
Score 1: Organization and connections between ideas and/or events are weak.
Score 0: No organization evident.
Style
Score 3: Command of language, including effective and compelling word choice and varied sentence structure, clearly supports the writer's purpose and audience.
Score 2: Adequate command of language, including effective word choice and clear sentences, supports the writer's purpose and audience.
Score 1: Limited use of language, including lack of variety in word choice and sentences, may hinder support for the writer's purpose and audience.
Score 0: Ineffective use of language for the writer's purpose and audience.
Conventions
Score 3: Consistent, appropriate use of conventions of Standard English for grammar, usage, spelling, capitalization, and punctuation for the grade level.
Score 2: Adequate use of conventions of Standard English for grammar, usage, spelling, capitalization, and punctuation for the grade level.
Score 1: Limited use of conventions of Standard English for grammar, usage, spelling, capitalization, and punctuation for the grade level.
Score 0: Ineffective use of conventions of Standard English for grammar, usage, spelling, capitalization, and punctuation.

Please total the points from each of the four traits. The maximum score is 15 points. (Idea score x 2) + Organization score + Style score + Conventions score = Total score out of 15 points.'''


SIMPLEST_ASAP_RUBRIC_7 = 'Based on the response\'s content, rate the response on a scale of 0 to 15.'


ASAP_RUBRIC_8 = '''A rating of 1-6 on the following four traits:
Ideas and Content
Score 6: The writing is exceptionally clear, focused, and interesting. It holds the reader’s attention throughout. Main ideas stand out and are developed by strong support and rich details suitable to audience and purpose. The writing is characterized by
- clarity, focus, and control.
- main idea(s) that stand out.
- supporting, relevant, carefully selected details; when appropriate, use of resources provides strong, accurate, credible support.
- a thorough, balanced, in-depth explanation / exploration of the topic; the writing makes connections and shares insights.
- content and selected details that are well-suited to audience and purpose.
Score 5: The writing is clear, focused and interesting. It holds the reader’s attention. Main ideas stand out and are developed by supporting details suitable to audience and purpose. The writing is characterized by
- clarity, focus, and control.
- main idea(s) that stand out.
- supporting, relevant, carefully selected details; when appropriate, use of resources provides strong, accurate, credible support.
- a thorough, balanced explanation / exploration of the topic; the writing makes connections and shares insights.
- content and selected details that are well-suited to audience and purpose.
Score 4: The writing is clear and focused. The reader can easily understand the main ideas. Support is present, although it may be limited or rather general. The writing is characterized by
- an easily identifiable purpose.
- clear main idea(s).
- supporting details that are relevant, but may be overly general or limited in places; when appropriate, resources are used to provide accurate support.
- a topic that is explored / explained, although developmental details may occasionally be out of balance with the main idea(s); some connections and insights may be present.
- content and selected details that are relevant, but perhaps not consistently well-chosen for audience and purpose.
Score 3: The reader can understand the main ideas, although they may be overly broad or simplistic, and the results may not be effective. Supporting detail is often limited, insubstantial, overly general, or occasionally slightly off-topic. The writing is characterized by
- an easily identifiable purpose and main idea(s).
- predictable or overly-obvious main ideas; or points that echo observations heard elsewhere; or a close retelling of another work.
- support that is attempted, but developmental details are often limited, uneven, somewhat off-topic, predictable, or too general (e.g., a list of underdeveloped points).
- details that may not be well-grounded in credible resources; they may be based on clichés, stereotypes or questionable sources of information.
- difficulties when moving from general observations to specifics.
Score 2: Main ideas and purpose are somewhat unclear or development is attempted but minimal. The writing is characterized by
- a purpose and main idea(s) that may require extensive inferences by the reader.
- minimal development; insufficient details.
- irrelevant details that clutter the text.
- extensive repetition of detail.
Score 1: The writing lacks a central idea or purpose. The writing is characterized by
- ideas that are extremely limited or simply unclear.
- attempts at development that are minimal or nonexistent; the paper is too short to demonstrate the development of an idea.
Organization
Score 6: The organization enhances the central idea(s) and its development. The order and structure are compelling and move the reader through the text easily. The writing is characterized by
- effective, perhaps creative, sequencing and paragraph breaks; the organizational structure fits the topic, and the writing is easy to follow.
- a strong, inviting beginning that draws the reader in and a strong, satisfying sense of resolution or closure.
- smooth, effective transitions among all elements (sentences, paragraphs, ideas).
- details that fit where placed.
Score 5: The organization enhances the central idea(s) and its development. The order and structure are strong and move the reader through the text. The writing is characterized by
- effective sequencing and paragraph breaks; the organizational structure fits the topic, and the writing is easy to follow.
- an inviting beginning that draws the reader in and a satisfying sense of resolution or closure.
- smooth, effective transitions among all elements (sentences, paragraphs, ideas).
- details that fit where placed.
Score 4: Organization is clear and coherent. Order and structure are present, but may seem formulaic. The writing is characterized by
- clear sequencing and paragraph breaks.
- an organization that may be predictable.
- a recognizable, developed beginning that may not be particularly inviting; a developed conclusion that may lack subtlety.
- a body that is easy to follow with details that fit where placed.
- transitions that may be stilted or formulaic.
- organization which helps the reader, despite some weaknesses.
Score 3: An attempt has been made to organize the writing; however, the overall structure is inconsistent or skeletal. The writing is characterized by
- attempts at sequencing and paragraph breaks, but the order or the relationship among ideas may occasionally be unclear.
- a beginning and an ending which, although present, are either undeveloped or too obvious (e.g., “My topic is...”; “These are all the reasons that...”).
- transitions that sometimes work. The same few transitional devices (e.g., coordinating conjunctions, numbering, etc.) may be overused.
- a structure that is skeletal or too rigid.
- placement of details that may not always be effective.
- organization which lapses in some places, but helps the reader in others.
Score 2: The writing lacks a clear organizational structure. An occasional organizational device is discernible; however, the writing is either difficult to follow and the reader has to reread substantial portions, or the piece is simply too short to demonstrate organizational skills. The writing is characterized by
- some attempts at sequencing, but the order or the relationship among ideas is frequently unclear; a lack of paragraph breaks.
- a missing or extremely undeveloped beginning, body, and/or ending.
- a lack of transitions, or when present, ineffective or overused.
- a lack of an effective organizational structure.
- details that seem to be randomly placed, leaving the reader frequently confused.
Score 1: The writing lacks coherence; organization seems haphazard and disjointed. Even after rereading, the reader remains confused. The writing is characterized by
- a lack of effective sequencing and paragraph breaks.
- a failure to provide an identifiable beginning, body and/or ending.
- a lack of transitions.
- pacing that is consistently awkward; the reader feels either mired down in trivia or rushed along too rapidly.
- a lack of organization which ultimately obscures or distorts the main point.
Sentence Fluency
Score 6: The writing has an effective flow and rhythm. Sentences show a high degree of craftsmanship, with consistently strong and varied structure that makes expressive oral reading easy and enjoyable. The writing is characterized by
- a natural, fluent sound; it glides along with one sentence flowing effortlessly into the next.
- extensive variation in sentence structure, length, and beginnings that add interest to the text.
- sentence structure that enhances meaning by drawing attention to key ideas or reinforcing relationships among ideas.
- varied sentence patterns that create an effective combination of power and grace.
- strong control over sentence structure; fragments, if used at all, work well.
- stylistic control; dialogue, if used, sounds natural.
Score 5: The writing has an easy flow and rhythm. Sentences are carefully crafted, with strong and varied structure that makes expressive oral reading easy and enjoyable. The writing is characterized by
- a natural, fluent sound; it glides along with one sentence flowing into the next.
- variation in sentence structure, length, and beginnings that add interest to the text.
- sentence structure that enhances meaning.
- control over sentence structure; fragments, if used at all, work well.
- stylistic control; dialogue, if used, sounds natural.
Score 4: The writing flows; however, connections between phrases or sentences may be less than fluid. Sentence patterns are somewhat varied, contributing to ease in oral reading. The writing is characterized by
- a natural sound; the reader can move easily through the piece, although it may lack a certain rhythm and grace.
- some repeated patterns of sentence structure, length, and beginnings that may detract somewhat from overall impact.
- strong control over simple sentence structures, but variable control over more complex sentences; fragments, if present, are usually effective.
- occasional lapses in stylistic control; dialogue, if used, sounds natural for the most part, but may at times sound stilted or unnatural.
Score 3: The writing tends to be mechanical rather than fluid. Occasional awkward constructions may force the reader to slow down or reread. The writing is characterized by
- some passages that invite fluid oral reading; however, others do not.
- some variety in sentence structure, length, and beginnings, although the writer falls into repetitive sentence patterns.
- good control over simple sentence structures, but little control over more complex sentences; fragments, if present, may not be effective.
- sentences which, although functional, lack energy.
- lapses in stylistic control; dialogue, if used, may sound stilted or unnatural.
- text that is too short to demonstrate variety and control.
Score 2: The writing tends to be either choppy or rambling. Awkward constructions often force the reader to slow down or reread. The writing is characterized by
- significant portions of the text that are difficult to follow or read aloud.
- sentence patterns that are monotonous (e.g., subject-verb or subject-verb-object).
- a significant number of awkward, choppy, or rambling constructions.
Score 1: The writing is difficult to follow or to read aloud. Sentences tend to be incomplete, rambling, or very awkward. The writing is characterized by
- text that does not invite—and may not even permit—smooth oral reading.
- confusing word order that is often jarring and irregular.
- sentence structure that frequently obscures meaning.
- sentences that are disjointed, confusing, or rambling.
Conventions
Score 6: The writing demonstrates exceptionally strong control of standard writing conventions (e.g., punctuation, spelling, capitalization, grammar and usage) and uses them effectively to enhance communication. Errors are so few and so minor that the reader can easily skim right over them unless specifically searching for them. The writing is characterized by
- strong control of conventions; manipulation of conventions may occur for stylistic effect.
- strong, effective use of punctuation that guides the reader through the text.
- correct spelling, even of more difficult words.
- correct grammar and usage that contribute to clarity and style.
- skill in using a wide range of conventions in a sufficiently long and complex piece.
- little or no need for editing.
Score 5: The writing demonstrates strong control of standard writing conventions (e.g., punctuation, spelling, capitalization, grammar and usage) and uses them effectively to enhance communication. Errors are few and minor. Conventions support readability. The writing is characterized by
- strong control of conventions.
- effective use of punctuation that guides the reader through the text.
- correct spelling, even of more difficult words.
- correct capitalization; errors, if any, are minor.
- correct grammar and usage that contribute to clarity and style.
- skill in using a wide range of conventions in a sufficiently long and complex piece.
- little need for editing.
Score 4: The writing demonstrates control of standard writing conventions (e.g., punctuation, spelling, capitalization, grammar and usage). Significant errors do not occur frequently. Minor errors, while perhaps noticeable, do not impede readability. The writing is characterized by
- control over conventions used, although a wide range is not demonstrated.
- correct end-of-sentence punctuation; internal punctuation may sometimes be incorrect.
- spelling that is usually correct, especially on common words.
- correct capitalization; errors, if any, are minor.
- occasional lapses in correct grammar and usage; problems are not severe enough to distort meaning or confuse the reader.
- moderate need for editing.
Score 3: The writing demonstrates limited control of standard writing conventions (e.g., punctuation, spelling, capitalization, grammar and usage). Errors begin to impede readability. The writing is characterized by
- some control over basic conventions; the text may be too simple or too short to reveal mastery.
- end-of-sentence punctuation that is usually correct; however, internal punctuation contains frequent errors.
- spelling errors that distract the reader; misspelling of common words occurs.
- capitalization errors.
- errors in grammar and usage that do not block meaning but do distract the reader.
- significant need for editing.
Score 2: The writing demonstrates little control of standard writing conventions. Frequent, significant errors impede readability. The writing is characterized by
- little control over basic conventions.
- many end-of-sentence punctuation errors; internal punctuation contains frequent errors.
- spelling errors that frequently distract the reader; misspelling of common words often occurs.
- capitalization that is inconsistent or often incorrect.
- errors in grammar and usage that interfere with readability and meaning.
- substantial need for editing.
Score 1: Numerous errors in usage, spelling, capitalization, and punctuation repeatedly distract the reader and make the text difficult to read. In fact, the severity and frequency of errors are so overwhelming that the reader finds it difficult to focus on the message and must reread for meaning. The writing is characterized by
- very limited skill in using conventions.
- basic punctuation (including end-of-sentence punctuation) that tends to be omitted, haphazard, or incorrect.
- frequent spelling errors that significantly impair readability.
- capitalization that appears to be random.
- a need for extensive editing.

Please total the points from each of the four traits. The maximum score is 30 points. Ideas and Content score + Organization score + Sentence Fluency score + 2 x Conventions score = Total score out of 30 points.
'''


SIMPLEST_ASAP_RUBRIC_8 = 'Based on the response\'s content, rate the response on a scale of 5 to 30.'


ASAP2_RUBRIC = '''After reading each essay and completing the analytical rating form, assign a holistic score based on the rubric below. For the following evaluations you will need to use a grading scale between 1 (minimum) and 6 (maximum). As with the analytical rating form, the distance between each grade (e.g., 1–2, 3–4, 4–5) should be considered equal.

SCORE OF 6: An essay in this category demonstrates clear and consistent mastery, although it may have a few minor errors. A typical essay effectively and insightfully develops a point of view on the issue and demonstrates outstanding critical thinking; the essay uses clearly appropriate examples, reasons, and other evidence taken from the source text(s) to support its position; the essay is well organized and clearly focused, demonstrating clear coherence and smooth progression of ideas; the essay exhibits skillful use of language, using a varied, accurate, and apt vocabulary and demonstrates meaningful variety in sentence structure; the essay is free of most errors in grammar, usage, and mechanics.

SCORE OF 5: An essay in this category demonstrates reasonably consistent mastery, although it will have occasional errors or lapses in quality. A typical essay effectively develops a point of view on the issue and demonstrates strong critical thinking; the essay generally using appropriate examples, reasons, and other evidence taken from the source text(s) to support its position; the essay is well organized and focused, demonstrating coherence and progression of ideas; the essay exhibits facility in the use of language, using appropriate vocabulary demonstrates variety in sentence structure; the essay is generally free of most errors in grammar, usage, and mechanics.

SCORE OF 4: An essay in this category demonstrates adequate mastery, although it will have lapses in quality. A typical essay develops a point of view on the issue and demonstrates competent critical thinking; the essay using adequate examples, reasons, and other evidence taken from the source text(s) to support its position; the essay is generally organized and focused, demonstrating some coherence and progression of ideas exhibits adequate; the essay may demonstrate inconsistent facility in the use of language, using generally appropriate vocabulary demonstrates some variety in sentence structure; the essay may have some errors in grammar, usage, and mechanics.

SCORE OF 3: An essay in this category demonstrates developing mastery, and is marked by ONE OR MORE of the following weaknesses: develops a point of view on the issue, demonstrating some critical thinking, but may do so inconsistently or use inadequate examples, reasons, or other evidence taken from the source texts to support its position; the essay is limited in its organization or focus, or may demonstrate some lapses in coherence or progression of ideas displays; the essay may demonstrate facility in the use of language, but sometimes uses weak vocabulary or inappropriate word choice and/or lacks variety or demonstrates problems in sentence structure; the essay may contain an accumulation of errors in grammar, usage, and mechanics.

SCORE OF 2: An essay in this category demonstrates little mastery, and is flawed by ONE OR MORE of the following weaknesses: develops a point of view on the issue that is vague or seriously limited, and demonstrates weak critical thinking; the essay providesinappropriate or insufficient examples, reasons, or other evidence taken from the source text to support its position; the essay is poorly organized and/or focused, or demonstrates serious problems with coherence or progression of ideas; the essay displays very little facility in the use of language, using very limited vocabulary or incorrect word choice and/or demonstrates frequent problems in sentence structure; the essay contains errors in grammar, usage, and mechanics so serious that meaning is somewhat obscured.

SCORE OF 1: An essay in this category demonstrates very little or no mastery, and is severely flawed by ONE OR MORE of the following weaknesses: develops no viable point of view on the issue, or provides little or no evidence to support its position; the essay is disorganized or unfocused, resulting in a disjointed orincoherent essay; the essay displays fundamental errors in vocabulary and/or demonstrates severe flaws in sentence structure; the essay contains pervasive errors in grammar, usage, or mechanics that persistently interfere with meaning.'''

SIMPLEST_ASAP2_RUBRIC = 'Based on the response\'s content, rate the response on a scale of 1 to 6.'


def prepare_asap_rubric(essay_set=1, seed_prompt='expert'):
    if essay_set == 1:
        if seed_prompt == 'expert':
            return ASAP_RUBRIC_1
        elif seed_prompt == 'simple':
            return SIMPLE_ASAP_RUBRIC_1
        elif seed_prompt == 'simplest':
            return SIMPLEST_ASAP_RUBRIC_1
        else:
            raise ValueError(f"No rubric defined for seed prompt {seed_prompt}")
    elif essay_set == 2:
        if seed_prompt == 'expert':
            return ASAP_RUBRIC_2
        elif seed_prompt == 'simple':
            return SIMPLE_ASAP_RUBRIC_2
        elif seed_prompt == 'simplest':
            return SIMPLEST_ASAP_RUBRIC_1 # Same as ASAP 1 for simplicity
        else:
            raise ValueError(f"No rubric defined for seed prompt {seed_prompt}")
    elif essay_set == 3:
        if seed_prompt == 'expert':
            return ASAP_RUBRIC_3
        elif seed_prompt == 'simple':
            return SIMPLE_ASAP_RUBRIC_3 
        elif seed_prompt == 'simplest':
            return SIMPLEST_ASAP_RUBRIC_3 
        else:
            raise ValueError(f"No rubric defined for seed prompt {seed_prompt}")
    elif essay_set == 4:
        if seed_prompt == 'expert':
            return ASAP_RUBRIC_3  # Same as ASAP 3
        elif seed_prompt == 'simple':
            return SIMPLE_ASAP_RUBRIC_3  # Same as ASAP 3
        elif seed_prompt == 'simplest':
            return SIMPLEST_ASAP_RUBRIC_3  # Same as ASAP 3
    elif essay_set == 5:
        if seed_prompt == 'expert':
            return ASAP_RUBRIC_5
        elif seed_prompt == 'simple':
            return ASAP_RUBRIC_5 # Same as expert
        elif seed_prompt == 'simplest':
            return SIMPLEST_ASAP_RUBRIC_5
    elif essay_set == 6:
        if seed_prompt == 'expert':
            return ASAP_RUBRIC_6
        elif seed_prompt == 'simple':
            return ASAP_RUBRIC_6 # Same as expert
        elif seed_prompt == 'simplest':
            return SIMPLEST_ASAP_RUBRIC_5 # Same as ASAP 5 simplest
    elif essay_set == 7:
        if seed_prompt == 'expert':
            return ASAP_RUBRIC_7
        elif seed_prompt == 'simple':
            return ASAP_RUBRIC_7 # Same as expert
        elif seed_prompt == 'simplest':
            return SIMPLEST_ASAP_RUBRIC_7 
    elif essay_set == 8:
        if seed_prompt == 'expert':
            return ASAP_RUBRIC_8
        elif seed_prompt == 'simple':
            return ASAP_RUBRIC_8 # Same as expert
        elif seed_prompt == 'simplest':
            return SIMPLEST_ASAP_RUBRIC_8 
    else:
        raise ValueError(f"No rubric defined for essay set {essay_set}")


def prepare_ets_rubric(dataset='ets', seed_prompt='expert'):
    if dataset == 'ets':
        if seed_prompt == 'expert':
            return ETS_RUBRIC
        elif seed_prompt == 'simple':
            return SIMPLE_ETS_RUBRIC
        elif seed_prompt == 'simplest':
            return SIMPLEST_ETS_RUBRIC
        else:
            raise ValueError(f"No rubric defined for seed prompt {seed_prompt}")
    elif dataset == 'ets3':
        if seed_prompt == 'expert':
            return ETS_RUBRIC_FOR_3
        elif seed_prompt == 'simple':
            return ETS_RUBRIC_FOR_3
        elif seed_prompt == 'simplest':
            return ETS_RUBRIC_FOR_3
        else:
            raise ValueError(f"No rubric defined for seed prompt {seed_prompt}")


def prepare_asap2_rubric(seed_prompt='expert'):
    if seed_prompt == 'expert':
        return ASAP2_RUBRIC
    elif seed_prompt == 'simple':
        return SIMPLEST_ASAP2_RUBRIC
    elif seed_prompt == 'simplest':
        return SIMPLEST_ASAP2_RUBRIC
    else:
        raise ValueError(f"No rubric defined for seed prompt {seed_prompt}")

ASAP_PROMPT_1 = '''More and more people use computers, but not everyone agrees that this benefits society. Those who support advances in technology believe that computers have a positive effect on people. They teach hand-eye coordination, give people the ability to learn about faraway places and people, and even allow people to talk online with other people. Others have different ideas. Some experts are concerned that people are spending too much time on their computers and less time exercising, enjoying nature, and interacting with family and friends. 

Write a letter to your local newspaper in which you state your opinion on the effects computers have on people. Persuade the readers to agree with you.'''


ASAP_PROMPT_2 = '''Censorship in the Libraries
"All of us can think of a book that we hope none of our children or any other children have taken off the shelf. But if I have the right to remove that book from the shelf -- that work I abhor -- then you also have exactly the same right and so does everyone else. And then we have no books left on the shelf for any of us." --Katherine Paterson, Author
Write a persuasive essay to a newspaper reflecting your vies on censorship in libraries. Do you believe that certain materials, such as books, music, movies, magazines, etc., should be removed from the shelves if they are found offensive? Support your position with convincing arguments from your own experience, observations, and/or reading.'''

ASAP_PROMPT_3 = '''Source Essay:
ROUGH ROAD AHEAD: Do Not Exceed Posted Speed Limit
by Joe Kurmaskie
FORGET THAT OLD SAYING ABOUT NEVER taking candy from strangers. No, a better piece of advice for the solo cyclist would be, “Never accept travel advice from a collection of old-timers who haven’t left the confines of their porches since Carter was in office.” It’s not that a group of old guys doesn’t know the terrain. With age comes wisdom and all that, but the world is a fluid place. Things change. 
At a reservoir campground outside of Lodi, California, I enjoyed the serenity of an early-summer evening and some lively conversation with these old codgers. What I shouldn’t have done was let them have a peek at my map. Like a foolish youth, the next morning I followed their advice and launched out at first light along a “shortcut” that was to slice away hours from my ride to Yosemite National Park.
They’d sounded so sure of themselves when pointing out landmarks and spouting off towns I would come to along this breezy jaunt. Things began well enough. I rode into the morning with strong legs and a smile on my face. About forty miles into the pedal, I arrived at the first “town.” This place might have been a thriving little spot at one time—say, before the last world war—but on that morning it fit the traditional definition of a ghost town. I chuckled, checked my water supply, and moved on. The sun was beginning to beat down, but I barely noticed it. The cool pines and rushing rivers of Yosemite had my name written all over them. 
Twenty miles up the road, I came to a fork of sorts. One ramshackle shed, several rusty pumps, and a corral that couldn’t hold in the lamest mule greeted me. This sight was troubling. I had been hitting my water bottles pretty regularly, and I was traveling through the high deserts of California in June.
I got down on my hands and knees, working the handle of the rusted water pump with all my strength. A tarlike substance oozed out, followed by brackish water feeling somewhere in the neighborhood of two hundred degrees. I pumped that handle for several minutes, but the water wouldn’t cool down. It didn’t matter. When I tried a drop or two, it had the flavor of battery acid.
The old guys had sworn the next town was only eighteen miles down the road. I could make that! I would conserve my water and go inward for an hour or so—a test of my inner spirit. 
Not two miles into this next section of the ride, I noticed the terrain changing. Flat road was replaced by short, rolling hills. After I had crested the first few of these, a large highway sign jumped out at me. It read: ROUGH ROAD AHEAD: DO NOT EXCEED POSTED SPEED LIMIT.
The speed limit was 55 mph. I was doing a water-depleting 12 mph. Sometimes life can feel so cruel. 
I toiled on. At some point, tumbleweeds crossed my path and a ridiculously large snake—it really did look like a diamondback—blocked the majority of the pavement in front of me. I eased past, trying to keep my balance in my dehydrated state.
The water bottles contained only a few tantalizing sips. Wide rings of dried sweat circled my shirt, and the growing realization that I could drop from heatstroke on a gorgeous day in June simply because I listened to some gentlemen who hadn’t been off their porch in decades, caused me to laugh.
It was a sad, hopeless laugh, mind you, but at least I still had the energy to feel sorry for myself. There was no one in sight, not a building, car, or structure of any kind. I began breaking the ride down into distances I could see on the horizon, telling myself that if I could make it that far, I’d be fi ne.
Over one long, crippling hill, a building came into view. I wiped the sweat from my eyes to make sure it wasn’t a mirage, and tried not to get too excited. With what I believed was my last burst of energy, I maneuvered down the hill.
In an ironic twist that should please all sadists reading this, the building—abandoned years earlier, by the looks of it—had been a Welch’s Grape Juice factory and bottling plant. A sandblasted picture of a young boy pouring a refreshing glass of juice into his mouth could still be seen.
I hung my head.
That smoky blues tune “Summertime” rattled around in the dry honeycombs of my deteriorating brain.
I got back on the bike, but not before I gathered up a few pebbles and stuck them in my mouth. I’d read once that sucking on stones helps take your mind off thirst by allowing what spit you have left to circulate. With any luck I’d hit a bump and lodge one in my throat.
It didn’t really matter. I was going to die and the birds would pick me clean, leaving only some expensive outdoor gear and a diary with the last entry in praise of old men, their wisdom, and their keen sense of direction. I made a mental note to change that paragraph if it looked like I was going to lose consciousness for the last time.
Somehow, I climbed away from the abandoned factory of juices and dreams, slowly gaining elevation while losing hope. Then, as easily as rounding a bend, my troubles, thirst, and fear were all behind me.
GARY AND WILBER’S FISH CAMP—IF YOU WANT BAIT FOR THE BIG ONES, WE’RE YOUR BEST BET!
“And the only bet,” I remember thinking.
As I stumbled into a rather modern bathroom and drank deeply from the sink, I had an overwhelming urge to seek out Gary and Wilber, kiss them, and buy some bait—any bait, even though I didn’t own a rod or reel.
An old guy sitting in a chair under some shade nodded in my direction. Cool water dripped from my head as I slumped against the wall beside him.
“Where you headed in such a hurry?”
“Yosemite,” I whispered.
“Know the best way to get there?”
I watched him from the corner of my eye for a long moment. He was even older than the group I’d listened to in Lodi.
“Yes, sir! I own a very good map.”
And I promised myself right then that I’d always stick to it in the future.
“Rough Road Ahead” by Joe Kurmaskie, from Metal Cowboy, copyright © 1999 Joe Kurmaskie.

Essay Prompt:
Write a response that explains how the features of the setting affect the cyclist. In your response, include examples from the essay that support your conclusion.
'''


ASAP_PROMPT_4 = '''Source Essay
Winter Hibiscus by Minfong Ho
Saeng, a teenage girl, and her family have moved to the United States from Vietnam. As Saeng walks home after failing her driver’s test, she sees a familiar plant. Later, she goes to a florist shop to see if the plant can be purchased.
It was like walking into another world. A hot, moist world exploding with greenery. Huge flat leaves, delicate wisps of tendrils, ferns and fronds and vines of all shades and shapes grew in seemingly random profusion.
“Over there, in the corner, the hibiscus. Is that what you mean?” The florist pointed at a leafy potted plant by the corner. 
There, in a shaft of the wan afternoon sunlight, was a single blood-red blossom, its five petals splayed back to reveal a long stamen tipped with yellow pollen. Saeng felt a shock of recognition so intense, it was almost visceral.1
“Saebba,” Saeng whispered.
A saebba hedge, tall and lush, had surrounded their garden, its lush green leaves dotted with vermilion flowers. And sometimes after a monsoon rain, a blossom or two would have blown into the well, so that when she drew the well water, she would find a red blossom floating in the bucket.
Slowly, Saeng walked down the narrow aisle toward the hibiscus. Orchids, lanna bushes, oleanders, elephant ear begonias, and bougainvillea vines surrounded her. Plants that she had not even realized she had known but had forgotten drew her back into her childhood world.
When she got to the hibiscus, she reached out and touched a petal gently. It felt smooth and cool, with a hint of velvet toward the center—just as she had known it would feel.
And beside it was yet another old friend, a small shrub with waxy leaves and dainty flowers with purplish petals and white centers. “Madagascar periwinkle,” its tag announced. How strange to see it in a pot, Saeng thought. Back home it just grew wild, jutting out from the cracks in brick walls or between tiled roofs.
And that rich, sweet scent—that was familiar, too. Saeng scanned the greenery around her and found a tall, gangly plant with exquisite little white blossoms on it.  “Dok Malik,” she said, savoring the feel of the word on her tongue, even as she silently noted the English name on its tag, “jasmine.”
One of the blossoms had fallen off, and carefully Saeng picked it up and smelled it. She closed her eyes and breathed in, deeply. The familiar fragrance filled her lungs, and Saeng could almost feel the light strands of her grandmother’s long gray hair, freshly washed, as she combed it out with the fine-toothed buffalo-horn comb. And when the sun had dried it, Saeng would help the gnarled old fingers knot the hair into a bun, then slip a dok Malik bud into it.
Saeng looked at the white bud in her hand now, small and fragile. Gently, she closed her palm around it and held it tight. That, at least, she could hold on to. But where was the fine-toothed comb? The hibiscus hedge? The well? Her gentle grandmother? 
A wave of loss so deep and strong that it stung Saeng’s eyes now swept over her. A blink, a channel switch, a boat ride into the night, and it was all gone. Irretrievably, irrevocably gone.
And in the warm moist shelter of the greenhouse, Saeng broke down and wept.
It was already dusk when Saeng reached home. The wind was blowing harder, tearing off the last remnants of green in the chicory weeds that were growing out of the cracks in the sidewalk. As if oblivious to the cold, her mother was still out in the vegetable garden, digging up the last of the onions with a rusty trowel. She did not see Saeng until the girl had quietly knelt down next to her.
Her smile of welcome warmed Saeng. “Ghup ma laio le? You’re back?” she said cheerfully. “Goodness, it’s past five. What took you so long? How did it go? Did you—?” Then she noticed the potted plant that Saeng was holding, its leaves quivering in the wind.
Mrs. Panouvong uttered a small cry of surprise and delight. “Dok faeng-noi!” she said. “Where did you get it?”
“I bought it,” Saeng answered, dreading her mother’s next question.
“How much?”
For answer Saeng handed her mother some coins.
“That’s all?” Mrs. Panouvong said, appalled, “Oh, but I forgot! You and the
Lambert boy ate Bee-Maags . . . .”
“No, we didn’t, Mother,” Saeng said.
“Then what else—?”
“Nothing else. I paid over nineteen dollars for it.”
“You what?” Her mother stared at her incredulously. “But how could you? All the seeds for this vegetable garden didn’t cost that much! You know how much we—” She paused, as she noticed the tearstains on her daughter’s cheeks and her puffy eyes.
“What happened?” she asked, more gently.
“I—I failed the test,” Saeng said.
For a long moment Mrs. Panouvong said nothing. Saeng did not dare look her mother in the eye. Instead, she stared at the hibiscus plant and nervously tore off a leaf, shredding it to bits.
Her mother reached out and brushed the fragments of green off Saeng’s hands. “It’s a beautiful plant, this dok faeng-noi,” she finally said. “I’m glad you got it.”
“It’s—it’s not a real one,” Saeng mumbled.
“I mean, not like the kind we had at—at—” She found that she was still too shaky to say the words at home, lest she burst into tears again. “Not like the kind we had before,” she said.
“I know,” her mother said quietly. “I’ve seen this kind blooming along the lake. Its flowers aren’t as pretty, but it’s strong enough to make it through the cold months here, this winter hibiscus. That’s what matters.”
She tipped the pot and deftly eased the ball of soil out, balancing the rest of the plant in her other hand. “Look how root-bound it is, poor thing,” she said. “Let’s plant it, right now.”
She went over to the corner of the vegetable patch and started to dig a hole in the ground. The soil was cold and hard, and she had trouble thrusting the shovel into it. Wisps of her gray hair trailed out in the breeze, and her slight frown deepened the wrinkles around her eyes. There was a frail, wiry beauty to her that touched Saeng deeply.
“Here, let me help, Mother,” she offered, getting up and taking the shovel away from her.
Mrs. Panouvong made no resistance. “I’ll bring in the hot peppers and bitter melons, then, and start dinner. How would you like an omelet with slices of the bitter melon?”
“I’d love it,” Saeng said.
Left alone in the garden, Saeng dug out a hole and carefully lowered the “winter hibiscus” into it. She could hear the sounds of cooking from the kitchen now, the beating of eggs against a bowl, the sizzle of hot oil in the pan. The pungent smell of bitter melon wafted out, and Saeng’s mouth watered. It was a cultivated taste, she had discovered—none of her classmates or friends, not even Mrs. Lambert, liked it—this sharp, bitter melon that left a golden aftertaste on the tongue. But she had grown up eating it and, she admitted to herself, much preferred it to a Big Mac.
The “winter hibiscus” was in the ground now, and Saeng tamped down the soil around it. Overhead, a flock of Canada geese flew by, their faint honks clear and—yes—familiar to Saeng now. Almost reluctantly, she realized that many of the things that she had thought of as strange before had become, through the quiet repetition of season upon season, almost familiar to her now. Like the geese. She lifted her head and watched as their distinctive V was etched against the evening sky, slowly fading into the distance.
When they come back, Saeng vowed silently to herself, in the spring, when the snows melt and the geese return and this hibiscus is budding, then I will take that test again.
“Winter Hibiscus” by Minfong Ho, copyright © 1993 by Minfong Ho, from Join In, Multiethnic Short Stories, by Donald R. Gallo, ed.

Essay Prompt:
Read the last paragraph of the story.

"When they come back, Saeng vowed silently to herself, in the spring, when the snows melt and the geese return and this hibiscus is budding, then I will take that test again." 

Write a response that explains why the author concludes the story with this paragraph. In your response, include details and examples from the story that support your ideas.'''


ASAP_PROMPT_5 = '''Source Essay:
Narciso Rodriguez
from Home: The Blueprints of Our Lives
My parents, originally from Cuba, arrived in the United States in 1956. After living for a year in a furnished one-room apartment, twenty-one-year-old Rawedia Maria and twenty-seven-year-old Narciso Rodriguez, Sr., could afford to move into a modest, three-room apartment I would soon call home.
In 1961, I was born into this simple house, situated in a two-family, blond-brick building in the Ironbound section of Newark, New Jersey. Within its walls, my young parents created our traditional Cuban home, the very heart of which was the kitchen. My parents both shared cooking duties and unwittingly passed on to me their rich culinary skills and a love of cooking that is still with me today (and for which I am eternally grateful). Passionate Cuban music (which I adore to this day) filled the air, mixing with the aromas of the kitchen. Here, the innocence of childhood, the congregation of family and friends, and endless celebrations that encompassed both, formed the backdrop to life in our warm home.
Growing up in this environment instilled in me a great sense that “family” had nothing to do with being a blood relative. Quite the contrary, our neighborhood was made up of mostly Spanish, Cuban, and Italian immigrants at a time when overt racism was the norm and segregation prevailed in the United States. In our neighborhood, despite customs elsewhere, all of these cultures came together in great solidarity and friendship. It was a close-knit community of honest, hardworking immigrants who extended a hand to people who, while not necessarily their own kind, were clearly in need.
Our landlord and his daughter, Alegria (my babysitter and first friend), lived above us, and Alegria graced our kitchen table for meals more often than not. Also at the table were Sergio and Edelmira, my surrogate grandparents who lived in the basement apartment. (I would not know my “real” grandparents, Narciso the Elder and Consuelo, until 1970 when they were allowed to leave Cuba.) My aunts Bertha and Juanita and my cousins Arnold, Maria, and Rosemary also all lived nearby and regularly joined us at our table. Countless extended family members came and went — and there was often someone staying with us temporarily until they were able to get back on their feet. My parents always kept their arms and their door open to the many people we considered family, knowing that they would do the same for us.
My mother and father had come to this country with such courage, without any knowledge of the language or the culture. They came selflessly, as many immigrants do, to give their children a better life, even though it meant leaving behind their families, friends, and careers in the country they loved. They struggled both personally and financially, braving the harsh northern winters while yearning for their native tropics and facing cultural hardships. The barriers to work were strong and high, and my parents both had to accept that they might not be able to find the kind of jobs they deserved. In Cuba, Narciso, Sr., had worked in a laboratory and Rawedia Maria had studied chemical engineering. In the United States, they had to start their lives over entirely, taking whatever work they could find. The faith that this struggle would lead them and their children to better times drove them to endure these hard times.
I will always be grateful to my parents for their love and sacrifice. I’ve often told them that what they did was a much more courageous thing than I could have ever done. I’ve often told them of my admiration for their strength and perseverance, and I’ve thanked them repeatedly. But, in reality, there is no way to express my gratitude for the spirit of generosity impressed upon me at such an early age and the demonstration of how important family and friends are. These are two lessons that my parents did not just tell me. They showed me with their lives, and these teachings have been the basis of my life.
It was in this simple house that my parents welcomed other refugees to celebrate their arrival to this country and where I celebrated my first birthdays. It was in the warmth of the kitchen in this humble house where a Cuban feast (albeit a frugal Cuban feast) always filled the air with not just scent and music but life and love. It was here where I learned the real definition of “family.” And for this, I will never forget that house or its gracious neighborhood or the many things I learned there about how to love. I will never forget how my parents turned this simple house into a home.
— Narciso Rodriguez, Fashion designer
Hometown: Newark, New Jersey
“Narciso Rodriguez” by Narciso Rodriguez, from Home: The Blueprints of Our Lives. Copyright © 2006 by John Edwards.

Essay Prompt:
Describe the mood created by the author in the memoir. Support your answer with relevant and specific information from the memoir.
'''


ASAP_PROMPT_6 = '''Source Essay:
The Mooring Mast
by Marcia Amidon Lüsted
When the Empire State Building was conceived, it was planned as the world’s tallest building, taller even than the new Chrysler Building that was being constructed at Forty-second Street and Lexington Avenue in New York. At seventy-seven stories, it was the tallest building before the Empire State began construction, and Al Smith was determined to outstrip it in height.
The architect building the Chrysler Building, however, had a trick up his sleeve. He secretly constructed a 185-foot spire inside the building, and then shocked the public and the media by hoisting it up to the top of the Chrysler Building, bringing it to a height of 1,046 feet, 46 feet taller than the originally announced height of the Empire State Building.
Al Smith realized that he was close to losing the title of world’s tallest building, and on December 11, 1929, he announced that the Empire State would now reach the height of 1,250 feet. He would add a top or a hat to the building that would be even more distinctive than any other building in the city. John Tauranac describes the plan:
[The top of the Empire State Building] would be more than ornamental, more than a spire or dome or a pyramid put there to add a desired few feet to the height of the building or to mask something as mundane as a water tank. Their top, they said, would serve a higher calling. The Empire State Building would be equipped for an age of transportation that was then only the dream of aviation pioneers.
This dream of the aviation pioneers was travel by dirigible, or zeppelin, and the Empire State Building was going to have a mooring mast at its top for docking these new airships, which would accommodate passengers on already existing transatlantic routes and new routes that were yet to come.
The Age of Dirigibles
By the 1920s, dirigibles were being hailed as the transportation of the future. Also known today as blimps, dirigibles were actually enormous steel-framed balloons, with envelopes of cotton fabric filled with hydrogen and helium to make them lighter than air. Unlike a balloon, a dirigible could be maneuvered by the use of propellers and rudders, and passengers could ride in the gondola, or enclosed compartment, under the balloon.
Dirigibles had a top speed of eighty miles per hour, and they could cruise at seventy miles per hour for thousands of miles without needing refueling. Some were as long as one thousand feet, the same length as four blocks in New York City. The one obstacle to their expanded use in New York City was the lack of a suitable landing area. Al Smith saw an opportunity for his Empire State Building: A mooring mast added to the top of the building would allow dirigibles to anchor there for several hours for refueling or service, and to let passengers off and on. Dirigibles were docked by means of an electric winch, which hauled in a line from the front of the ship and then tied it to a mast. The body of the dirigible could swing in the breeze, and yet passengers could safely get on and off the dirigible by walking down a gangplank to an open observation platform.
The architects and engineers of the Empire State Building consulted with experts, taking tours of the equipment and mooring operations at the U.S. Naval Air Station in Lakehurst, New Jersey. The navy was the leader in the research and development of dirigibles in the United States. The navy even offered its dirigible, the Los Angeles, to be used in testing the mast. The architects also met with the president of a recently formed airship transport company that planned to offer dirigible service across the Pacific Ocean.
When asked about the mooring mast, Al Smith commented:
[It’s] on the level, all right. No kidding. We’re working on the thing now. One set of engineers here in New York is trying to dope out a practical, workable arrangement and the Government people in Washington are figuring on some safe way of mooring airships to this mast.
Designing the Mast
The architects could not simply drop a mooring mast on top of the Empire State Building’s flat roof. A thousand-foot dirigible moored at the top of the building, held by a single cable tether, would add stress to the building’s frame. The stress of the dirigible’s load and the wind pressure would have to be transmitted all the way to the building’s foundation, which was nearly eleven hundred feet below. The steel frame of the Empire State Building would have to be modified and strengthened to accommodate this new situation. Over sixty thousand dollars’ worth of modifications had to be made to the building’s framework.
Rather than building a utilitarian mast without any ornamentation, the architects designed a shiny glass and chrome-nickel stainless steel tower that would be illuminated from inside, with a stepped-back design that imitated the overall shape of the building itself. The rocket-shaped mast would have four wings at its corners, of shiny aluminum, and would rise to a conical roof that would house the mooring arm. The winches and control machinery for the dirigible mooring would be housed in the base of the shaft itself, which also housed elevators and stairs to bring passengers down to the eighty-sixth floor, where baggage and ticket areas would be located.
The building would now be 102 floors, with a glassed-in observation area on the 101st floor and an open observation platform on the 102nd floor. This observation area was to double as the boarding area for dirigible passengers.
Once the architects had designed the mooring mast and made changes to the existing plans for the building’s skeleton, construction proceeded as planned. When the building had been framed to the 85th floor, the roof had to be completed before the framing for the mooring mast could take place. The mast also had a skeleton of steel and was clad in stainless steel with glass windows. Two months after the workers celebrated framing the entire building, they were back to raise an American flag again—this time at the top of the frame for the mooring mast.
The Fate of the Mast
The mooring mast of the Empire State Building was destined to never fulfill its purpose, for reasons that should have been apparent before it was ever constructed. The greatest reason was one of safety: Most dirigibles from outside of the United States used hydrogen rather than helium, and hydrogen is highly flammable. When the German dirigible Hindenburg was destroyed by fire in Lakehurst, New Jersey, on May 6, 1937, the owners of the Empire State Building realized how much worse that accident could have been if it had taken place above a densely populated area such as downtown New York.
The greatest obstacle to the successful use of the mooring mast was nature itself. The winds on top of the building were constantly shifting due to violent air currents. Even if the dirigible were tethered to the mooring mast, the back of the ship would swivel around and around the mooring mast. Dirigibles moored in open landing fields could be weighted down in the back with lead weights, but using these at the Empire State Building, where they would be dangling high above pedestrians on the street, was neither practical nor safe.
The other practical reason why dirigibles could not moor at the Empire State Building was an existing law against airships flying too low over urban areas. This law would make it illegal for a ship to ever tie up to the building or even approach the area, although two dirigibles did attempt to reach the building before the entire idea was dropped. In December 1930, the U.S. Navy dirigible Los Angeles approached the mooring mast but could not get close enough to tie up because of forceful winds. Fearing that the wind would blow the dirigible onto the sharp spires of other buildings in the area, which would puncture the dirigible’s shell, the captain could not even take his hands off the control levers. 
Two weeks later, another dirigible, the Goodyear blimp Columbia, attempted a publicity stunt where it would tie up and deliver a bundle of newspapers to the Empire State Building. Because the complete dirigible mooring equipment had never been installed, a worker atop the mooring mast would have to catch the bundle of papers on a rope dangling from the blimp. The papers were delivered in this fashion, but after this stunt the idea of using the mooring mast was shelved. In February 1931, Irving Clavan of the building’s architectural office said, “The as yet unsolved problems of mooring air ships to a fixed mast at such a height made it desirable to postpone to a later date the final installation of the landing gear.”
By the late 1930s, the idea of using the mooring mast for dirigibles and their passengers had quietly disappeared. Dirigibles, instead of becoming the transportation of the future, had given way to airplanes. The rooms in the Empire State Building that had been set aside for the ticketing and baggage of dirigible passengers were made over into the world’s highest soda fountain and tea garden for use by the sightseers who flocked to the observation decks. The highest open observation deck, intended for disembarking passengers, has never been open to the public.
“The Mooring Mast” by Marcia Amidon Lüsted, from The Empire State Building. Copyright © 2004 by Gale, a part of Cengage Learning, Inc.

Essay Prompt:
Based on the excerpt, describe the obstacles the builders of the Empire State Building faced in attempting to allow dirigibles to dock there. Support your answer with relevant and specific information from the excerpt.'''

ASAP_PROMPT_7 = '''Write about patience. Being patient means that you are understanding and tolerant. A patient person experience difficulties without complaining.
Do only one of the following: write a story about a time when you were patient OR write a story about a time when someone you know was patient OR write a story in your own way about patience.'''


ASAP_PROMPT_8 = "We all understand the benefits of laughter. For example, someone once said, “Laughter is the shortest distance between two people.” Many other people believe that laughter is an important part of any relationship. Tell a true story in which laughter was one element or part."

ASAP2_PROMPT = '''Source text:
{source_text}

Essay Prompt:
{essay_prompt}'''


def prepare_prompt_for_asap(essay_set=1):
    if essay_set == 1:
        return ASAP_PROMPT_1
    elif essay_set == 2:
        return ASAP_PROMPT_2
    elif essay_set == 3:
        return ASAP_PROMPT_3
    elif essay_set == 4:
        return ASAP_PROMPT_4
    elif essay_set == 5:
        return ASAP_PROMPT_5
    elif essay_set == 6:
        return ASAP_PROMPT_6
    elif essay_set == 7:
        return ASAP_PROMPT_7
    elif essay_set == 8:
        return ASAP_PROMPT_8
    else:
        raise ValueError(f"Unsupported essay_set: {essay_set}")
    

if __name__ == "__main__":
    print(repr(ASAP_RUBRIC_1))
    print(ASAP_RUBRIC_1)