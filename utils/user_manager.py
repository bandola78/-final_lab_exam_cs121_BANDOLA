import os
from utils.user import User


class UserManager:
    def __init__(self):
        self.users = {}    # as an empty dictionary
        self.load_users()  # invocation of load_users() method

    def load_users(self):
        try:
            with open("data/users.txt", "r") as file:
                for line in file:
                    username, password = line.strip().split(",")
                    self.users[username] = User(username, password)

        except FileNotFoundError:
            # creates a data folder if not present yet, and generates a users.txt file in it
            os.makedirs("data", exist_ok=True)
            with open("data/users.txt", "w") as file:
                pass

    def save_users(self):
        with open("data/users.txt", "w") as file:
            for username, user_object in self.users.items():
                file.write(f"{username},{user_object.password}\n")

    def validate_username(self, username):
        if len(username) < 4:
            return False
        return True

    def validate_password(self, password):
        if len(password) < 8:
            return False
        return True

    def register_user(self, user):
        if user.username in self.users:
            print("Username already exists.")
            return False
        if not self.validate_username(user.username):
            print("Username must be at least 4 characters long.")
            return False
        if not self.validate_password(user.password):
            print("Password must be at least 8 characters long.")
            return False
        self.users[user.username] = User(user.username, user.password)
        self.save_users()
        print("Registration successful.")
        return True

    def login_user(self, user):
        if user.username in self.users and self.users[user.username].password == user.password:
            print(f"Welcome, {user.username}!")
            return True
        else:
            print("Invalid username or password. Please try again.")
            return False