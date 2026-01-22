from npc_brain import load_knowledge, npc_reply

class NPC:
    def __init__(self, name, role, knowledge_path):
        self.name = name
        self.role = role
        self.knowledge, self.index = load_knowledge(knowledge_path)
        self.memory = []

    def talk(self, text):
        return npc_reply(
            text,
            self.knowledge,
            self.index,
            self.memory,
            self.role
        )



class NPCManager:
    def __init__(self):
        self.npcs = {}

    def add_npc(self, npc_id, role, knowledge_path):
        self.npcs[npc_id] = NPC(npc_id, role, knowledge_path)


    def talk_to(self, npc_id, text):
        return self.npcs[npc_id].talk(text)
