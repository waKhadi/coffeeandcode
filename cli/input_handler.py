def get_workshop_details():
    print("\n--- Coffee & Code Workshop Details ---\n")

    def prompt(field):
        while True:
            value = input(f"{field}: ").strip()
            if value:
                return value
            print(f"{field} cannot be empty. Try again.")

    return {
        "name": prompt("Workshop Name"),
        "date": prompt("Date (e.g. 20 April 2026)"),
        "time": prompt("Time (e.g. 10:00 AM)"),
        "summary": prompt("Summary"),
        "description": prompt("Description")
    }