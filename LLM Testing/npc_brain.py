import ollama
from rag import retrieve
from behavior import get_state
from prompt import build_prompt
from memory import ConversationMemory
import os
os.environ["TRANSFORMERS_OFFLINE"] = "1"

memory = ConversationMemory()

def npc_reply(user_input, trust=0.3, threatened=False):
    state = get_state(trust, threatened)
    knowledge = retrieve(user_input)

    context = memory.get_context()

    prompt = build_prompt(
        state=state,
        trust=trust,
        knowledge=knowledge,
        context=context,
        user_input=user_input
    )

    response = ollama.chat(
        model="llama3.1:8b",
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response["message"]["content"]

    # Store conversation
    memory.add("Player", user_input)
    memory.add("Tirumala", reply)

    return reply
