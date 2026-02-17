from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import streamlit as st

base_model_name = "google/flan-t5-base"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(base_model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(base_model_name)
    return tokenizer, model

tokenizer, model = load_model()

def generate(prompt, max_length=256):

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=max_length,
            temperature=0.8,
            top_p=0.9,
            do_sample=True
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
