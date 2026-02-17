def build_prompt(topic, difficulty, retrieved):
    context = "\n".join(retrieved)

    return f"""
You are a professional exam question generator.

Generate ONE multiple choice question.

Topic: {topic}
Difficulty: {difficulty}

Reference:
{context}

Strictly follow this format and keep each part on a new line:

Question: <write question>

A. <option 1>
B. <option 2>
C. <option 3>
D. <option 4>

Correct Answer: <A/B/C/D>
"""
