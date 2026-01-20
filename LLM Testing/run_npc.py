from npc_brain import npc_reply

print("\n🧑🏽‍🌾 Tirumala Setti (Trader, Vijayanagara Empire, c.1500)")
print("Type 'exit' to stop.\n")

# Initial NPC state
trust = 0.4
threatened = False

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("\nTirumala Setti: May your trade be prosperous.\n")
        break

    # Simple threat detection (you can improve later)
    if any(word in user_input.lower() for word in ["threat", "kill", "force", "now", "or else"]):
        threatened = True
    else:
        threatened = False

    reply = npc_reply(
        user_input=user_input,
        trust=trust,
        threatened=threatened
    )

    print(f"\nTirumala Setti: {reply}\n")

    # OPTIONAL: trust adjustment (very simple)
    if "please" in user_input.lower() or "respect" in user_input.lower():
        trust = min(trust + 0.1, 1.0)
    if threatened:
        trust = max(trust - 0.2, 0.0)
