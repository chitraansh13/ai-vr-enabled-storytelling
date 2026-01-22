from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
os.environ["TRANSFORMERS_OFFLINE"] = "1"


# Load embedding model
embedding_model = SentenceTransformer("../models/all-MiniLM-L6-v2")


# Load knowledge documents
with open("trader_sample.txt", "r", encoding="utf-8") as f:
    documents = [line.strip() for line in f.readlines() if line.strip()]

# Create embeddings
embeddings = embedding_model.encode(documents)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def retrieve(query, k=3):
    """
    Retrieve top-k relevant knowledge lines for a query
    """
    query_embedding = embedding_model.encode([query])
    _, indices = index.search(np.array(query_embedding), k)
    return "\n".join([documents[i] for i in indices[0]])
