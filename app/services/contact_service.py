import json

from app.json_encoder import ContactAwareJSONEncoder
from app.models import Contact


class ContactService:
    def __init__(self, filename):
        self.contacts = []
        self.filename = filename

        self.load_contacts()

    def get_count(self):
        return len(self.contacts)

    def get_contacts(self):
        return self.contacts

    def find(self, term):
        results = []
        for contact in self.contacts:
            if term.lower() in contact.name.lower() or term.lower() in contact.email.lower():
                results.append(contact)

        return results

    def create(self, name, email):
        contact = Contact(name, email)

        self.contacts.append(contact)
        self.save_contacts()

        return contact

    def update(self, id_, name, email):
        for num, contact in enumerate(self.contacts, start=1):
            if num == id_:
                contact.name = name if name else contact.name
                contact.email = email if email else contact.email

                self.save_contacts()

    def remove(self, id_):
        del self.contacts[id_ - 1]
        self.save_contacts()

    def load_contacts(self):
        with open(self.filename) as f:
            contacts = json.load(f)

            # self.contacts = [Contact(contact["name"], contact["email"]) for contact in contacts]
            # Contact(name="...", email="...")
            self.contacts = [Contact(**contact) for contact in contacts]

    def save_contacts(self):
        data = json.dumps(self.contacts, indent=2, cls=ContactAwareJSONEncoder)
        with open(self.filename, "w") as f:
            f.write(data)
