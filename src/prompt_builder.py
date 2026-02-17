def build_prompt(topic, difficulty, retrieved):
    context = "\n".join(retrieved)

    return f"""
You are an expert exam creator.

Reference examples:
{context}

Create a high-quality MCQ.

Topic: {topic}
Difficulty: {difficulty}

Format:
Question:
A.
B.
C.
D.
Answer:
"""
