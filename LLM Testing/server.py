from fastapi import FastAPI
from pydantic import BaseModel
from npc_brain import npc_reply

app = FastAPI()

# simple session memory
trust = 0.4

class PlayerInput(BaseModel):
    text: str

@app.post("/chat")
def chat(data: PlayerInput):
    global trust

    threatened = any(
        word in data.text.lower()
        for word in ["threat", "force", "now", "or else"]
    )

    reply = npc_reply(
        user_input=data.text,
        trust=trust,
        threatened=threatened
    )

    # simple trust update
    if "please" in data.text.lower():
        trust = min(trust + 0.1, 1.0)
    if threatened:
        trust = max(trust - 0.2, 0.0)

    return {"reply": reply}
