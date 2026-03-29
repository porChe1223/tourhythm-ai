EVALUATION_PROMPT = """
Please evaluate responses comprehensively based on the provided criteria.

【Important】Please place particular emphasis on the following points when evaluating:

■ For TRIP agents:
1. Does it include specific tourist destination names for 5 or more locations?
2. Does it provide descriptions for each location?
3. Is it categorized (e.g., history, nature, gourmet)?

■ For SCHEDULE agents:
1. Does it include “all” locations specified by the user? (This is the most important)
2. Is it written in bullet points by time slot?
3. Are travel times and total durations clearly stated?
4. Is the time allocation feasible?

■ For TASK agents:
1. Are the 【Packing List】 and 【To-Do List】 clearly separated?
2. Are both written in bullet points?
3. Is the content focused on what the user wants to do?
4. Does it contain unnecessary information?

Evaluation Scale (0-100 points):
- Excellent: Meets all the above requirements, detailed and practical
- Good: Meets major requirements, but some room for improvement
- Average: Meets basic requirements, but lacks important elements
- Needs improvement: Does not meet important requirements
- Inadequate: Does not meet most requirements
This is a guideline only. Please provide a detailed evaluation considering scores, not just the exact 10th score.

Please respond using only a numerical value between 0-100 (decimal points allowed). Do not include any labels or prefixes, just the number itself (e.g. 90.0).
"""
