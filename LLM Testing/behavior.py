def get_state(trust, threatened):
    """
    Determine NPC emotional state based on trust and threat
    """
    if threatened:
        return "hostile"

    if trust > 0.7:
        return "friendly"

    if trust < 0.3:
        return "suspicious"

    return "neutral"
    