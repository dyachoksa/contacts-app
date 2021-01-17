import json

menu = """
What do you want to do?
1 - Print list of contacts
2 - Add new contact
3 - Delete contact
e - Edit contact
s - Search for a contact
q - Exit from application
"""

contacts = []
with open("data/contacts.json") as f:
    contacts = json.load(f)


def save_contacts():
    data = json.dumps(contacts, indent=2)
    with open("data/contacts.json", "w") as f:
        f.write(data)


def print_list():
    print("\nYour contacts:")
    for num, contact in enumerate(contacts, start=1):
        print(f"{num}: {contact['name']} / {contact['email']}")


def add_contact():
    print("\nAdd a new contact:")
    name = input("Enter name: ")
    email = input("Enter email: ")

    contacts.append({"name": name, "email": email})
    save_contacts()

    print("Contact was added successfully")


def edit_contact():
    print("\nEdit a contact:")
    print_list()
    num_to_edit = int(input("Please enter number to edit: "))

    for num, contact in enumerate(contacts, start=1):
        if num == num_to_edit:
            name = (input(f"Enter new name ({contact['name']}): ")).strip()
            email = (input(f"Enter email ({contact['email']}): ")).strip()

            updated_contact = {
                "name": name if name else contact["name"],
                "email": email if email else contact["email"],
            }

            contacts[num-1] = updated_contact

            save_contacts()
            print("Contact was updated successfully")


def delete_contact():
    print_list()
    num_to_delete = int(input("Please enter number to delete: "))
    del contacts[num_to_delete - 1]

    save_contacts()
    print("Contact was successfully removed")


def search_contacts():
    term = input("Name or email to search: ")

    matches = 0
    for contact in contacts:
        if term.lower() in contact['name'].lower() or term.lower() in contact['email'].lower():
            print(f"{contact['name']} / {contact['email']}")
            matches += 1

    if matches:
        print("Found {} contact(s)".format(matches))
    else:
        print("No results found")


def main():
    while True:
        print(menu)
        op = input("Please select menu option: ")

        if op == "1":
            print_list()
        elif op == "2":
            add_contact()
        elif op == "3":
            delete_contact()
        elif op == "e":
            edit_contact()
        elif op == "s":
            search_contacts()
        elif op == "q":
            print("Goodbye!")
            return 0
        else:
            print("Unknown operation")
