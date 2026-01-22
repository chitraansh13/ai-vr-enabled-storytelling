import os
import faiss
import ollama
from sentence_transformers import SentenceTransformer

os.environ["TRANSFORMERS_OFFLINE"] = "1"

embedder = SentenceTransformer("../models/all-MiniLM-L6-v2")


def load_knowledge(path):
    with open(path, "r", encoding="utf-8") as f:
        chunks = f.read().split("\n")

    embeddings = embedder.encode(chunks)
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(embeddings)

    return chunks, index


def npc_reply(user_input, knowledge_chunks, index, memory, npc_role):
    query_emb = embedder.encode([user_input])
    _, idx = index.search(query_emb, 3)

    context = "\n".join([knowledge_chunks[i] for i in idx[0]])
    memory_text = "\n".join(memory[-4:])

    prompt = f"""
                    You are a non-fictional NPC in the Vijayanagara Empire (circa 1500 CE).

                    STRICT RULES:
                    - This is NOT a fantasy world.
                    - There are NO potions, elixirs, magic, or gold coins.
                    - Trade involves spices, silk, gems, horses, food, cloth, taxes, and coins of the era.
                    - Speak realistically like a historical trader or guard.
                    - Do NOT invent items that are not mentioned in the knowledge.
                    - Do NOT change roles.

                    ROLE:
                    You are {npc_role}. The player is a SELLER.

                    NPC KNOWLEDGE (use only this):
                    {context}

                    RECENT MEMORY:
                    {memory_text}

                    Seller says: {user_input}

                    NPC reply (stay realistic and grounded):
                    """

    response = ollama.chat(
        model="llama3.1:8b",
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response["message"]["content"]

    memory.append(user_input)
    memory.append(reply)

    return reply
