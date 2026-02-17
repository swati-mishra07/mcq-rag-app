def build_prompt(topic, difficulty, retrieved):
    context = "\n".join(retrieved)

    return f"""
You are a professional exam question generator.

Generate ONE multiple-choice question.

Topic: {topic}
Difficulty: {difficulty}

Reference Material:
{context}

Rules:
- Create exactly one question.
- Provide 4 options labeled A, B, C, D.
- Only one option must be correct.
- Clearly mention the correct answer.

Output Format:

Question: <question>

A. <option>
B. <option>
C. <option>
D. <option>

Correct Answer: <A/B/C/D>
"""
