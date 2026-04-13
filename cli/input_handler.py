def get_workshop_details():
    print("\n--- Coffee & Code Workshop Details ---\n")

    name = input("Workshop Name: ")
    date = input("Date (e.g. 20 April 2026): ")
    time = input("Time (e.g. 10:00 AM): ")
    summary = input("Summary: ")
    description = input("Description: ")

    return {
        "name": name,
        "date": date,
        "time": time,
        "summary": summary,
        "description": description
    }