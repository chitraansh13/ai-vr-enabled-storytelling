class MarketState:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)
        # keep only last 5 events to avoid prompt bloat
        self.events = self.events[-5:]

    def get_context(self):
        if not self.events:
            return "No recent market events."
        return "\n".join(self.events)
