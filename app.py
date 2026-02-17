import streamlit as st
from src.model_loader import generate
from src.rag_retriever import RAGRetriever
from src.prompt_builder import build_prompt


def main():
    retriever = RAGRetriever()

    st.title("🧠 Adaptive RAG MCQ Generator")

    topic = st.text_input("Enter Topic")
    difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])

    if st.button("Generate"):

        retrieved = retriever.retrieve(topic)
        prompt = build_prompt(topic, difficulty, retrieved)
        output = generate(prompt)

        st.text_area("Generated Question", output, height=300)


if __name__ == "__main__":
    main()
