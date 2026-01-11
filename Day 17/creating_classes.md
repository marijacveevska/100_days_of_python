- Pascal Case is naming where you capitalize each first letter : PascalCaseVariable (USED FOR CLASSES)
- Camel Case is naming where the first letter is lower case but each next word is Uppercase : camelCaseVariable
- Snake Case is where everything is lower case but split by _ : snake_case_variable


class User:
    # Constructor / Initializing and Object
    def __init__(self):
    # initialize attributes
        print("New user is being initialized")

user_1 = User()

# Creating attributes (variables)
user_1.id = "001"
user_1.username = "marija"

print(user_1.username)

# OR

class User:
    # Constructor / Initializing and Object
    def __init__(self,user_id,username):
    # initialize attributes
        print("New user is being initialized")
        self.id = user_id
        self.username = username

user_1 = User("001","marija")

