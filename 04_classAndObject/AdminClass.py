from UserClass import User

# inherit class User
class Admin(User):
    
    def __init__(self):
        super().__init__()
        print("I am an admin")

    def say_hello(self):
        print("Hello from Admin")
