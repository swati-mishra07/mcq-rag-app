import streamlit as st
import time
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from src.model_loader import generate
from src.rag_retriever import RAGRetriever
from src.prompt_builder import build_prompt
from src.evaluation import evaluate_generation


# ------------------------------
# Streamlit Page Config
# ------------------------------
st.set_page_config(
    page_title="Adaptive RAG MCQ Generator",
    layout="wide"
)

st.title("🧠 Adaptive RAG MCQ Generator")
st.markdown("Retrieval-Augmented MCQ Generation with Base vs LoRA Model Comparison")


# ------------------------------
# Load Base Model (Cached)
# ------------------------------
@st.cache_resource
def load_base_model():
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
    return tokenizer, model


base_tokenizer, base_model = load_base_model()


# ------------------------------
# Initialize Retriever
# ------------------------------
retriever = RAGRetriever()


# ------------------------------
# User Inputs
# ------------------------------
topic = st.text_input("Enter Topic")
difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])


# ------------------------------
# Generate Button
# ------------------------------
if st.button("Generate"):

    if not topic:
        st.warning("Please enter a topic.")
        st.stop()

    with st.spinner("Generating MCQs..."):

        # ------------------------------
        # Retrieve Context
        # ------------------------------
        retrieved = retriever.retrieve(topic)

        if not retrieved:
            st.error("No relevant context retrieved.")
            st.stop()

        st.markdown("### 📚 Retrieved Context")
        st.write(retrieved)

        # ------------------------------
        # Build Prompt
        # ------------------------------
        prompt = build_prompt(topic, difficulty, retrieved)

        st.markdown("---")

        # ==================================================
        # BASE MODEL GENERATION
        # ==================================================
        base_start = time.time()

        base_inputs = base_tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True
        )

        base_outputs = base_model.generate(
            **base_inputs,
            max_length=256
        )

        base_output = base_tokenizer.decode(
            base_outputs[0],
            skip_special_tokens=True
        )

        base_time = round(time.time() - base_start, 3)

        # ==================================================
        # LoRA MODEL GENERATION
        # ==================================================
        lora_start = time.time()

        lora_output = generate(prompt)

        lora_time = round(time.time() - lora_start, 3)

    # ==================================================
    # Display Model Comparison
    # ==================================================
    st.markdown("## 🔍 Model Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Base Model Output")
        st.write(base_output)
        st.info(f"Inference Time: {base_time} sec")

    with col2:
        st.markdown("### LoRA Fine-tuned Output")
        st.write(lora_output)
        st.info(f"Inference Time: {lora_time} sec")

    # ==================================================
    # Evaluation Section
    # ==================================================
    st.markdown("---")
    st.markdown("## 📊 Evaluation Section")

    reference_text = st.text_area(
        "Optional: Enter reference answer for evaluation"
    )

    if reference_text:

        base_scores = evaluate_generation(base_output, reference_text)
        lora_scores = evaluate_generation(lora_output, reference_text)

        col3, col4 = st.columns(2)

        with col3:
            st.markdown("### Base Model Metrics")
            st.json(base_scores)

        with col4:
            st.markdown("### LoRA Model Metrics")
            st.json(lora_scores)
