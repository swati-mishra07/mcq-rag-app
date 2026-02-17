# 🧠 MCQ Generator using RAG + LoRA Fine-Tuning

An AI-powered web application that generates context-aware Multiple Choice Questions (MCQs) using Retrieval-Augmented Generation (RAG) and a LoRA fine-tuned Large Language Model.

---

## 🚀 Project Highlights

- 🔹 LoRA fine-tuned FLAN-T5 model
- 🔹 Retrieval-Augmented Generation (RAG)
- 🔹 Semantic search using sentence embeddings
- 🔹 Modular backend architecture
- 🔹 Interactive Streamlit interface
- 🔹 Lightweight and efficient fine-tuning approach

---

## 🏗️ Architecture Overview

User Input
↓
Retriever (Sentence Transformer + FAISS)
↓
Context Builder (Prompt Engineering)
↓
LoRA Fine-Tuned FLAN-T5
↓
Generated MCQ Output


---

## 🛠️ Tech Stack

- Python
- Streamlit
- HuggingFace Transformers
- PEFT (LoRA)
- Sentence-Transformers
- FAISS
- PyTorch

---

## 📂 Project Structure

mcq-rag-app/
│
├── app.py # Streamlit UI
├── src/
│ ├── model_loader.py # Loads base model + LoRA
│ ├── rag_retriever.py # Semantic retrieval logic
│ └── prompt_builder.py # Prompt engineering
│
├── requirements.txt
├── README.md
└── .gitignore


---

## ⚙️ Installation

1️⃣ Clone Repository
```bash
git clone https://github.com/swati-mishra07/mcq-rag-lora-app.git
cd mcq-rag-lora-app


2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
streamlit run app.py


---

## 🧠 Model Details

| Component            | Description |
|----------------------|-------------|
| **Base Model**       | google/flan-t5-base |
| **Fine-Tuning**      | LoRA (Low-Rank Adaptation) |
| **Embedding Model**  | sentence-transformers/all-MiniLM-L6-v2 |

⚠️ LoRA adapter weights are excluded due to GitHub file size limitations.

---

## 📊 Why LoRA?

LoRA enables parameter-efficient fine-tuning by updating only a small subset of model parameters instead of the entire network.

### ✅ Key Benefits

- Reduced memory usage  
- Faster training  
- Lower deployment cost  
- Efficient domain adaptation  

---

## 📈 Real-World Applications

- EdTech platforms  
- Automated assessment systems  
- Exam preparation tools  
- AI-driven content generation  
- Learning management systems  

---

## 🔮 Future Improvements

- Deploy to HuggingFace Spaces  
- Add evaluation metrics (BLEU / ROUGE)  
- Build REST API endpoint  
- Implement authentication system  
- Optimize inference via model merging  
- Add logging & monitoring  

---

## 👩‍💻 Author

**Swati Mishra**  
GitHub: https://github.com/swati-mishra07  

---
