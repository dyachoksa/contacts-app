class Contact:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Contact name={self.name} email={self.email}>"

    def get_display_value(self) -> str:
        return f"{self.name} / {self.email}"

    def has_email(self) -> bool:
        return self.email is not None and len(self.email) > 0

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
        }
