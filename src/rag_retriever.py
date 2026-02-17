import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

class RAGRetriever:
    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.read_index("arc_faiss.index")
        self.df = pd.read_csv("arc_data.csv")

    def retrieve(self, query, top_k=3):
        query_embedding = self.embedder.encode([query])
        distances, indices = self.index.search(
            np.array(query_embedding), top_k
        )
        return self.df.iloc[indices[0]]["question"].tolist()
