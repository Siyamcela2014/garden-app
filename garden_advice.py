"""Provide gardening advice based on the month and season.

TODO: Refactor the advice into reusable functions.
TODO: Add input validation for month values.
TODO: Replace hardcoded advice with a reusable data structure.
"""


def get_season(month):
    """Return the season for a month in the Southern Hemisphere."""
    seasons = {
        12: "Summer", 1: "Summer", 2: "Summer",
        3: "Autumn", 4: "Autumn", 5: "Autumn",
        6: "Winter", 7: "Winter", 8: "Winter",
        9: "Spring", 10: "Spring", 11: "Spring",
    }
    return seasons.get(month, "Unknown")


def get_gardening_advice(month):
    """Return gardening advice for a given month."""
    advice = {
        1: "Water plants regularly and protect them from extreme heat.",
        2: "Harvest ripe vegetables and check plants for pests.",
        3: "Prepare soil and plant suitable autumn vegetables.",
        4: "Add compost to garden beds and reduce watering as needed.",
        5: "Protect sensitive plants as temperatures begin to fall.",
        6: "Prune suitable plants and prepare garden tools for winter.",
        7: "Plan spring planting and remove weeds.",
        8: "Prepare seedbeds and start planting spring vegetables.",
        9: "Plant seasonal flowers and monitor new growth.",
        10: "Water consistently and watch for garden pests.",
        11: "Mulch garden beds to help retain moisture.",
        12: "Keep plants hydrated and harvest summer crops.",
    }
    return advice.get(month, "Please enter a month from 1 to 12.")


def main():
    """Run the gardening advice application."""
    try:
        month = int(input("Enter the month (1-12): "))
        if not 1 <= month <= 12:
            print("Invalid month. Enter a number from 1 to 12.")
            return

        print(f"Season: {get_season(month)}")
        print(f"Gardening advice: {get_gardening_advice(month)}")
    except ValueError:
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
