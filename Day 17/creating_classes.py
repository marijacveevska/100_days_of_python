# Instagram Users
class User:
    def __init__(self,user_id,username):
        print("New user is being initialized")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1


user_1 = User("001","MarijaC")
user_2 = User("002","JackB")

print(user_1.username)
print(user_1.id)
print(user_1.followers)

user_1.follow(user_2)
print(f"{user_1.username} followers: {user_1.followers}")
print(f"{user_1.username} following: {user_1.following}")
print(f"{user_2.username} followers: {user_2.followers}")
print(f"{user_2.username} following: {user_2.following}")

user_2.follow(user_1)

print(f"{user_1.username} followers: {user_1.followers}")
print(f"{user_1.username} following: {user_1.following}")
print(f"{user_2.username} followers: {user_2.followers}")
print(f"{user_2.username} following: {user_2.following}")