def allocate_resources(severity, population):

    multiplier = {
        "Low": 1,
        "Moderate": 2,
        "High": 4
    }

    factor = multiplier.get(severity, 1)

    return {
        "ambulances": factor * 2,
        "rescue_teams": factor * 3,
        "food_packets": population * factor,
        "medical_kits": factor * 5
    }