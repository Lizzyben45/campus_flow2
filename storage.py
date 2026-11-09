import json
import os

FILE_PATH = "tickets.json"


def load_tickets():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as file:
        content = file.read()

    if not content.strip():
        return []

    try:
        tickets = json.loads(content)
    except json.JSONDecodeError:
        raise ValueError("tickets.json contains invalid JSON.")

    if not isinstance(tickets, list):
        raise ValueError("Ticket storage must contain a JSON list.")

    return tickets


def save_tickets(tickets):
    with open(FILE_PATH, "w") as file:
        json.dump(tickets, file, indent=4)