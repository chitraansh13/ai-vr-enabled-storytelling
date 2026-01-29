from npc_manager import NPCManager

manager = NPCManager()

npc_map = {
    "1": "trader_a",
    "2": "trader_b",
    "3": "trader_c",
    "4": "guard"
}

manager.add_npc("trader_a", "Trader A (aggressive buyer)", "npcs/trader_a/knowledge.txt")
manager.add_npc("trader_b", "Trader B (polite buyer)", "npcs/trader_b/knowledge.txt")
manager.add_npc("trader_c", "Trader C (suspicious buyer)", "npcs/trader_c/knowledge.txt")
manager.add_npc("guard", "Market Guard", "npcs/guard/knowledge.txt")

while True:
    print("\nWho do you want to talk to?")
    print("1 - Trader A")
    print("2 - Trader B")
    print("3 - Trader C")
    print("4 - Guard")

    choice = input("Enter number: ").strip()
    if choice not in npc_map:
        print("Invalid choice.")
        continue

    msg = input("You (Seller): ")
    npc_id = npc_map[choice]
    print("NPC:", manager.talk_to(npc_id, msg))
