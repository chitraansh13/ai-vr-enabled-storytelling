from npc_manager import NPCManager

manager = NPCManager()

manager.add_npc(
    "trader_a",
    "Trader A, an aggressive spice and gemstone buyer",
    "npcs/trader_a/knowledge.txt"
)

manager.add_npc(
    "trader_b",
    "Trader B, a polite long-term buyer",
    "npcs/trader_b/knowledge.txt"
)

manager.add_npc(
    "trader_c",
    "Trader C, a suspicious negotiator",
    "npcs/trader_c/knowledge.txt"
)

manager.add_npc(
    "guard",
    "Market Guard enforcing lawful trade",
    "npcs/guard/knowledge.txt"
)


while True:
    npc = input("\nTalk to (trader_a / trader_b / trader_c / guard): ")
    msg = input("You (Seller): ")
    print("NPC:", manager.talk_to(npc, msg))
