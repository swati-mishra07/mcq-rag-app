import streamlit as st
import time
import torch
import os
import evaluate
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from peft import PeftModel


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="Adaptive RAG MCQ Generator", layout="wide")
st.title("📚 Adaptive RAG MCQ Generator")
st.markdown("Compare Base Model vs LoRA Fine-Tuned Model")


# --------------------------------------------------
# LOAD MODELS (SAFE CACHE)
# --------------------------------------------------
@st.cache_resource(show_spinner=False)
def load_models():

    base_model_name = "google/flan-t5-base"
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    tokenizer = AutoTokenizer.from_pretrained(base_model_name)

    base_model = AutoModelForSeq2SeqLM.from_pretrained(
        base_model_name,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    ).to(device)

    lora_path = os.path.join(os.getcwd(), "mcq_lora_model")

    lora_model = PeftModel.from_pretrained(
        base_model,
        lora_path
    ).to(device)

    base_model.eval()
    lora_model.eval()

    return tokenizer, base_model, lora_model, device


tokenizer, base_model, lora_model, device = load_models()


# --------------------------------------------------
# LOAD METRICS (CACHE ONCE)
# --------------------------------------------------
@st.cache_resource(show_spinner=False)
def load_metrics():
    return {
        "bleu": evaluate.load("bleu"),
        "rouge": evaluate.load("rouge"),
        "bertscore": evaluate.load("bertscore"),
    }

metrics = load_metrics()


# --------------------------------------------------
# SIMPLE RETRIEVER
# --------------------------------------------------
class SimpleRetriever:
    def retrieve(self, query):
        return f"Context related to {query}"

retriever = SimpleRetriever()


# --------------------------------------------------
# PROMPT BUILDER
# --------------------------------------------------
def build_prompt(topic, difficulty, context):
    return f"""
Generate 3 {difficulty} level multiple choice questions about {topic}.

Context:
{context}

Format:
Q1:
A)
B)
C)
D)
Answer:
"""


# --------------------------------------------------
# GENERATION FUNCTION
# --------------------------------------------------
def generate(model, prompt):

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True
    ).to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=256
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# --------------------------------------------------
# EVALUATION FUNCTION
# --------------------------------------------------
def evaluate_generation(prediction, reference):

    bleu_score = metrics["bleu"].compute(
        predictions=[prediction],
        references=[[reference]]
    )

    rouge_score = metrics["rouge"].compute(
        predictions=[prediction],
        references=[reference]
    )

    bert_score = metrics["bertscore"].compute(
        predictions=[prediction],
        references=[reference],
        lang="en"
    )

    return {
        "BLEU": round(bleu_score["bleu"], 4),
        "ROUGE-L": round(rouge_score["rougeL"], 4),
        "BERTScore-F1": round(sum(bert_score["f1"]) / len(bert_score["f1"]), 4)
    }


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------
topic = st.text_input("Enter Topic")
difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])


# --------------------------------------------------
# SESSION STATE INIT
# --------------------------------------------------
if "results" not in st.session_state:
    st.session_state.results = None


# --------------------------------------------------
# GENERATE BUTTON
# --------------------------------------------------
if st.button("Generate"):

    if not topic:
        st.warning("Please enter a topic.")
        st.stop()

    with st.spinner("Generating MCQs..."):

        context = retriever.retrieve(topic)
        prompt = build_prompt(topic, difficulty, context)

        # Base model
        start = time.time()
        base_output = generate(base_model, prompt)
        base_time = round(time.time() - start, 3)

        # LoRA model
        start = time.time()
        lora_output = generate(lora_model, prompt)
        lora_time = round(time.time() - start, 3)

        st.session_state.results = {
            "base_output": base_output,
            "lora_output": lora_output,
            "base_time": base_time,
            "lora_time": lora_time
        }


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------
if st.session_state.results:

    data = st.session_state.results

    st.markdown("---")
    st.markdown("## 🔍 Model Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Base Model Output")
        st.write(data["base_output"])
        st.info(f"Inference Time: {data['base_time']} sec")

    with col2:
        st.markdown("### LoRA Fine-Tuned Output")
        st.write(data["lora_output"])
        st.info(f"Inference Time: {data['lora_time']} sec")

    st.markdown("---")
    st.markdown("## 📊 Evaluation Section")

    reference_text = st.text_area("Optional: Enter reference answer for evaluation")

    if reference_text:

        base_scores = evaluate_generation(
            data["base_output"],
            reference_text
        )

        lora_scores = evaluate_generation(
            data["lora_output"],
            reference_text
        )

        col3, col4 = st.columns(2)

        with col3:
            st.markdown("### Base Model Metrics")
            st.json(base_scores)

        with col4:
            st.markdown("### LoRA Model Metrics")
            st.json(lora_scores)
