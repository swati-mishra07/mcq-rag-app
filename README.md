# 🧠 Adaptive LoRA Fine-Tuned MCQ Generator

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-orange)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![PEFT](https://img.shields.io/badge/PEFT-LoRA-green)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)

---

## 📸 Application Demo

![App Demo](assets/app_demo.png)

---

## 🚀 Project Overview

This project implements a **LoRA fine-tuned Large Language Model pipeline** for automatic Multiple Choice Question (MCQ) generation.

It compares:

- Base model performance
- LoRA fine-tuned model performance
- Inference speed
- Automatic NLP evaluation metrics

The system demonstrates practical LLM optimization using parameter-efficient fine-tuning.

---

## 🧠 Base Model

- **Model:** google/flan-t5-base
- Framework: Hugging Face Transformers
- Fine-Tuning: LoRA (Low-Rank Adaptation) using PEFT

---

## ⚙️ System Architecture

```
                ┌────────────────────┐
                │   User Input Text  │
                └─────────┬──────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │   FLAN-T5 Tokenizer  │
               └─────────┬────────────┘
                         │
         ┌───────────────┴───────────────┐
         ▼                               ▼
┌───────────────────┐           ┌───────────────────┐
│   Base FLAN-T5    │           │  LoRA Fine-Tuned  │
│     Model         │           │       Model       │
└─────────┬─────────┘           └─────────┬─────────┘
          │                                 │
          ▼                                 ▼
   Generated MCQ                     Generated MCQ
          │                                 │
          └──────────────┬──────────────────┘
                         ▼
               ┌────────────────────┐
               │ Evaluation Module  │
               │ BLEU / ROUGE /     │
               │ BERTScore          │
               └────────────────────┘
```

---

## 📊 Evaluation Metrics

The system automatically evaluates generated MCQs using:

- BLEU
- ROUGE-L
- BERTScore (semantic similarity)

This provides both lexical and semantic quality comparison.

---

## 🔬 Technical Stack

- Python 3.10
- PyTorch
- Transformers (Hugging Face)
- PEFT (LoRA)
- Sentence-Transformers
- FAISS (vector similarity support)
- Streamlit (frontend UI)

---

## 📁 Project Structure

```
mcq-rag-app/
│
├── app.py
├── requirements.txt
├── mcq_lora_model/
│   ├── adapter_config.json
│   └── adapter_model.safetensors
├── assets/
│   └── app_demo.png
└── README.md
```

---

## 🖥️ Run Locally

```bash
git clone https://github.com/swati-mishra07/mcq-rag-app.git
cd mcq-rag-app

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
```

---

## 💡 Key ML Concepts Demonstrated

- Parameter Efficient Fine-Tuning (LoRA)
- Transformer-based Sequence-to-Sequence models
- Model comparison benchmarking
- Inference latency measurement
- NLP automatic evaluation metrics
- Modular ML application design

---

## 📈 Real-World Applications

- AI-based education systems
- Automated assessment generation
- EdTech platforms
- Curriculum design automation
- Smart content generation tools

---

## 🧪 Future Improvements

- Full Retrieval-Augmented Generation (RAG) pipeline
- Batch dataset benchmarking
- REST API deployment
- Model quantization for faster inference
- Production-grade Docker containerization

---

## 👩‍💻 Author

Swati Mishra  
Computer Science (IT) Undergraduate  
Machine Learning & AI Enthusiast  

GitHub: https://github.com/swati-mishra07