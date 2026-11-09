from storage import save_tickets, load_tickets


def create_ticket(tickets):
    print("\n===== SELECT TICKET CATEGORY =====")
    print("1. Network Issue")
    print("2. Software Issue")
    print("3. Hardware Issue")

    category_choices = {
        "1": "Network Issue",
        "2": "Software Issue",
        "3": "Hardware Issue"
    }

    category_choice = input("\nSelect a category: ").strip()

    if category_choice not in category_choices:
        print("Invalid category selection.")
        return

    category = category_choices[category_choice]

    title = input("\nEnter ticket title: ").strip() 

    if not title:
        print("Error: Ticket title cannot be empty.")
        return

    description = input("Enter ticket description: ").strip()
    
    if not description:
        print("Error: Ticket description cannot be empty.")
        return

    if tickets:
        next_id = max(ticket["id"] for ticket in tickets) + 1
    else:
        next_id = 1

    new_ticket = {
        "id": next_id,
        "category": category,
        "title": title,
        "description": description
    }

    tickets.append(new_ticket)

    try:
        save_tickets(tickets)
        print(f"\nTicket created successfully! ID: {next_id}")

    except OSError:
        tickets.pop()
        print("Error: Unable to save ticket.")


def view_tickets(tickets):
    if not tickets:
        print("\nNo tickets available.")
        return

    print("\n===== SAVED TICKETS =====")

    for ticket in tickets:
        print("-------------------------")
        print(f"ID: {ticket['id']}")
        print(f"Category: {ticket.get('category', 'Uncategorized')}")
        print(f"Title: {ticket['title']}")
        print(f"Description: {ticket['description']}")

    print("-------------------------")


def main():
    try:
        tickets = load_tickets()

    except (ValueError, OSError) as error:
        print(f"Storage error: {error}")
        return

    while True:
        print("\n===== CAMPUSFLOW 2 =====")
        print("1. Create Ticket")
        print("2. View All Tickets")
        print("3. Save Tickets")
        print("4. Load Tickets")
        print("5. Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            create_ticket(tickets)

        elif choice == "2":
            view_tickets(tickets)

        elif choice == "3":
            try:
                save_tickets(tickets)
                print("\nTickets saved successfully!")

            except OSError:
                print("\nError: Unable to save tickets.")

        elif choice == "4":
            try:
                tickets = load_tickets()
                print("\nTickets loaded successfully!")
                view_tickets(tickets)

            except (ValueError, OSError) as error:
                print(f"\nError loading tickets: {error}")

        elif choice == "5":
            print("\nThank you for using CampusFlow 2!")
            break

        else:
            print("\nInvalid selection. Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()