import json


class ContactsManager:
    def __init__(self, filename="data/contacts.json"):
        self.contacts = []
        self.filename = filename
        self.load_contacts()

    def __str__(self):
        return "Contacts Manager"

    def __len__(self):
        return self.get_contacts_count()

    def get_contacts_count(self):
        return len(self.contacts)

    def load_contacts(self):
        with open(self.filename) as f:
            self.contacts = json.load(f)

    def save_contacts(self):
        data = json.dumps(self.contacts, indent=2)
        with open(self.filename, "w") as f:
            f.write(data)

    def print_list(self):
        print("\nYour contacts:")
        for num, contact in enumerate(self.contacts, start=1):
            print(f"{num}: {contact['name']} / {contact['email']}")

    def add_contact(self):
        print("\nAdd a new contact:")
        name = input("Enter name: ")
        email = input("Enter email: ")

        self.contacts.append({"name": name, "email": email})
        self.save_contacts()

        print("Contact was added successfully")

    def edit_contact(self):
        print("\nEdit a contact:")
        self.print_list()
        num_to_edit = int(input("Please enter number to edit: "))

        for num, contact in enumerate(self.contacts, start=1):
            if num == num_to_edit:
                name = (input(f"Enter new name ({contact['name']}): ")).strip()
                email = (input(f"Enter email ({contact['email']}): ")).strip()

                updated_contact = {
                    "name": name if name else contact["name"],
                    "email": email if email else contact["email"],
                }

                self.contacts[num-1] = updated_contact

                self.save_contacts()
                print("Contact was updated successfully")

    def delete_contact(self):
        self.print_list()
        num_to_delete = int(input("Please enter number to delete: "))
        del self.contacts[num_to_delete - 1]

        self.save_contacts()
        print("Contact was successfully removed")

    def search_contacts(self):
        term = input("Name or email to search: ")

        matches = 0
        for contact in self.contacts:
            if term.lower() in contact['name'].lower() or term.lower() in contact['email'].lower():
                print(f"{contact['name']} / {contact['email']}")
                matches += 1

        if matches:
            print("Found {} contact(s)".format(matches))
        else:
            print("No results found")
