import json
import os

def load_tickets():
    if not os.path.exists("tickets.json"):
        return [] 

    with open("tickets.json", "r") as file:
        tickets = load_tickets()

    return tickets

def save_tickets(tickets):
    with open("tickets.json", "w") as file:
        json.dump(tickets, file, indent=4)
