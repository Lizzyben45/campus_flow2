from storage import save_tickets, load_tickets 

tickets = [
    {
    "id": 1,
    "title": "Login issue",
    "description": "i cannot log into my account"
    }
]

save_tickets(tickets)
saved_tickets = load_tickets()
print(saved_tickets)