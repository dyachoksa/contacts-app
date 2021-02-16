import typing

from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"


class UserService:
    def __init__(self):
        self.users = [
            User(1, "admin", "123456"),
            User(2, "sergey", "password"),
        ]

    def get_by_id(self, user_id) -> typing.Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user

        return None

    def get_by_username(self, username) -> typing.Optional[User]:
        for user in self.users:
            if user.username == username:
                return user

        return None
