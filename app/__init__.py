import sys

from .contacts_cli import ContactsCLI

menu = """
What do you want to do?
l - Print list of contacts
a - Add new contact
d - Delete contact
e - Edit contact
s - Search for a contact
q - Exit from application
"""


def main():
    filename = "data/contacts.json"

    if len(sys.argv) > 1:
        filename = sys.argv[1]

    print("Using database:", filename)
    manager = ContactsCLI(filename)

    while True:
        print(menu)
        print(f"Total contacts: {len(manager)}")
        op = input("Please select menu option: ")

        if op == "l":
            manager.print_list()
        elif op == "a":
            manager.add_contact()
        elif op == "d":
            manager.delete_contact()
        elif op == "e":
            manager.edit_contact()
        elif op == "s":
            manager.search_contacts()
        elif op == "q":
            print("Goodbye!")
            return 0
        else:
            print("Unknown operation")
