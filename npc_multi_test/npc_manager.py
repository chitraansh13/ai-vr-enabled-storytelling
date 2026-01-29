from npc_brain import load_knowledge, npc_reply
from market_state import MarketState

class NPC:
    def __init__(self, name, role, knowledge_path, market_state):
        self.name = name
        self.role = role
        self.knowledge, self.index = load_knowledge(knowledge_path)
        self.memory = []
        self.market_state = market_state

    def talk(self, text):
        reply = npc_reply(
            text,
            self.knowledge,
            self.index,
            self.memory,
            self.role,
            self.market_state.get_context()
        )

        # record what this NPC said
        self.market_state.add_event(
            f"{self.role} said: {reply}"
        )

        return reply


class NPCManager:
    def __init__(self):
        self.npcs = {}
        self.market_state = MarketState()

    def add_npc(self, npc_id, role, knowledge_path):
        self.npcs[npc_id] = NPC(
            npc_id,
            role,
            knowledge_path,
            self.market_state
        )

    def talk_to(self, npc_id, text):
        # record player action
        self.market_state.add_event(f"Seller said: {text}")
        return self.npcs[npc_id].talk(text)
