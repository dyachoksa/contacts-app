from .services.contact_service import ContactService


class ContactsCLI:
    def __init__(self, filename: str = "data/contacts.json"):
        self.contacts_service = ContactService(filename)

    def __str__(self):
        return "Contacts Manager"

    def __len__(self):
        return self.contacts_service.get_count()

    def get_contacts_count(self):
        return self.contacts_service.get_count()

    def print_list(self):
        print("\nYour contacts:")
        for num, contact in enumerate(self.contacts_service.get_contacts(), start=1):
            print(f"{num}: {contact.get_display_value()}")

    def add_contact(self):
        print("\nAdd a new contact:")
        name = input("Enter name: ")
        email = input("Enter email: ")

        self.contacts_service.create(name, email)

        print("Contact was added successfully")

    def edit_contact(self):
        print("\nEdit a contact:")
        self.print_list()
        num_to_edit = int(input("Please enter number to edit: "))

        name = (input(f"Enter new name (leave it blank to not change): ")).strip()
        email = (input(f"Enter email (leave it blank to not change): ")).strip()

        self.contacts_service.update(num_to_edit, name, email)

        print("Contact was updated successfully")

    def delete_contact(self):
        self.print_list()
        num_to_delete = int(input("Please enter number to delete: "))

        self.contacts_service.remove(num_to_delete)

        print("Contact was successfully removed")

    def search_contacts(self):
        term = input("Name or email to search: ")

        results = self.contacts_service.find(term)

        if results:
            print("Found {} contact(s)".format(len(results)))
            for contact in results:
                print(contact.get_display_value())
        else:
            print("No results found")
