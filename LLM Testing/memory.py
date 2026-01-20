class ConversationMemory:
    def __init__(self, max_turns=6):
        self.max_turns = max_turns
        self.history = []

    def add(self, speaker, text):
        self.history.append(f"{speaker}: {text}")
        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def get_context(self):
        return "\n".join(self.history)
