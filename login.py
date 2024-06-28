from .constants import USERNAME, PASSWORD

def login(user, password):
    if user == USERNAME and password == PASSWORD:
        print("logged in successfully")


def logout():
    print("user logged out successfully")