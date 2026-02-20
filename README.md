---
title: Adaptive RAG MCQ Generator
emoji: 🧠
colorFrom: indigo
colorTo: blue
sdk: streamlit
sdk_version: "1.32.2"
app_file: app.py
pinned: false
---

# 🧠 Adaptive LoRA Fine-Tuned MCQ Generator

A Streamlit-based NLP application that compares a base sequence-to-sequence model with a LoRA fine-tuned variant for automatic MCQ generation.

The system evaluates model outputs using BLEU, ROUGE, and BERTScore metrics and benchmarks inference time.


## 🚀 Features

🤖 Base Model: google/flan-t5-base

🎯 LoRA Fine-Tuning using PEFT

📊 Automatic Evaluation (BLEU, ROUGE-L, BERTScore)

⚡ Inference Time Comparison

🌐 Interactive Streamlit Web Interface

---

## 🏗️ Project Structure
mcq-rag-app/
│
├── app.py
├── requirements.txt
├── mcq_lora_model/
│   ├── adapter_config.json
│   └── adapter_model.bin / .safetensors
└── README.md

---

## 📊 Evaluation Metrics

The system compares generated MCQs using:

BLEU

ROUGE-L

BERTScore (semantic similarity)

Metrics are computed against a user-provided reference answer.


---

## 🧪 Model Comparison

The app compares:

Base FLAN-T5 Model

LoRA Fine-Tuned Model

Across:

Output quality

Inference time

Automatic evaluation metrics

---

## 🖥️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

---

## 📈 Real-World Applications

Educational content generation

Automated assessment systems

EdTech platforms

AI-assisted curriculum design

  
---

## 🔮 Future Improvements

Implement real Retrieval-Augmented Generation (FAISS-based)

Batch dataset evaluation

Visualization dashboards

REST API deployment

Model merging for optimized inference

---

## 👩‍💻 Author

**Swati Mishra**  
GitHub: https://github.com/swati-mishra07  

---
