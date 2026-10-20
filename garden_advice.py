
"""Provide gardening advice based on the month and season.

This module offers seasonal gardening guidance for the
Southern Hemisphere.
"""

# Gardening advice is stored in one reusable data structure.
GARDENING_ADVICE = {
    1: "Water plants regularly and protect them from extreme heat.",
    2: "Keep watering plants and harvest summer vegetables.",
    3: "Prepare soil and plant cool-season vegetables.",
    4: "Add compost and protect plants as temperatures drop.",
    5: "Reduce watering and plant winter vegetables.",
    6: "Protect sensitive plants from cold and frost.",
    7: "Prune suitable plants and prepare soil for spring.",
    8: "Start preparing beds and sow early spring vegetables.",
    9: "Plant spring flowers and increase watering gradually.",
    10: "Plant warm-season crops and remove weeds.",
    11: "Water deeply and mulch beds to retain moisture.",
    12: "Water frequently and protect plants from summer heat.",
}

# Each month is mapped to its Southern Hemisphere season.
SEASONS = {
    1: "Summer", 2: "Summer", 3: "Autumn",
    4: "Autumn", 5: "Autumn", 6: "Winter",
    7: "Winter", 8: "Winter", 9: "Spring",
    10: "Spring", 11: "Spring", 12: "Summer",
}


def validate_month(month):
    """Return True when month is an integer from 1 to 12."""
    return isinstance(month, int) and not isinstance(
        month, bool
    ) and 1 <= month <= 12


def get_season(month):
    """Return the season for a valid month in the Southern Hemisphere."""
    if not validate_month(month):
        raise ValueError("Month must be an integer between 1 and 12.")

    return SEASONS[month]


def get_gardening_advice(month):
    """Return gardening advice for a valid month."""
    if not validate_month(month):
        raise ValueError("Month must be an integer between 1 and 12.")

    return GARDENING_ADVICE[month]


def main():
    """Ask for a month and display its season and gardening advice."""
    try:
        month = int(input("Enter a month (1-12): "))
        season = get_season(month)
        advice = get_gardening_advice(month)

        print(f"\nSeason: {season}")
        print(f"Gardening advice: {advice}")

    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
