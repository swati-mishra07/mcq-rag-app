import streamlit as st
from src.model_loader import generate
from src.rag_retriever import retriever
from src.prompt_builder import build_prompt


def main():
    st.title("🧠 Adaptive RAG MCQ Generator")

    topic = st.text_input("Enter Topic")
    difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])

    if st.button("Generate"):

        retrieved = retriever.retrieve(topic)
        st.write("Retrieved:", retrieved)
        prompt = build_prompt(topic, difficulty, retrieved)
        output = generate(prompt)

        st.markdown("### Generated Question")
        st.markdown(output)



if __name__ == "__main__":
    main()
