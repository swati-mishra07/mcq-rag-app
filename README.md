# 🧠 Adaptive LoRA Fined-Tuned MCQ Generator

Built a LoRA fine-tuned MCQ generation system comparing base and adapted models using evaluation metrics (BLEU, ROUGE, BERTScore) with Streamlit deployment.

- 🔎 FAISS-based semantic retrieval
- 🤖 FLAN-T5 Base
- 🎯 LoRA Fine-Tuning (PEFT)
- 📊 Automatic Evaluation (ROUGE, BLEU, BERTScore)
- ⚡ Inference Time Benchmarking
- 🌐 Streamlit Web Interface

---

## 🚀 Features

- RAG-based context retrieval
- Base vs LoRA model comparison
- Inference time logging
- Automatic evaluation metrics
- Modular architecture
- Research-style evaluation pipeline

---

## 🏗️ Project Structure
mcq-rag-app/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│ ├── model_loader.py
│ ├── rag_retriever.py
│ ├── prompt_builder.py
│ └── evaluation.py
│
└── data/


---

## 📊 Evaluation Metrics

- ROUGE-L
- BLEU
- BERTScore (Semantic Similarity)

---

## 🧪 Model Comparison

The system compares:

- Base FLAN-T5
- LoRA Fine-Tuned Model

Including:
- Output quality
- Inference time
- Metric scores

---

## 🖥️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

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
