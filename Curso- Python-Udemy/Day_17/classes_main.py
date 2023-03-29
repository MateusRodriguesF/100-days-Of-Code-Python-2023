# class User:
#     pass

# user_1 = User()
# user_1.id = "001"
# user_1.username = "tteus"

# print(user_1.username)

# Using the Initialize in the constructor

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User(0, "Mateus")
user_2 = User(1, "Matthews")

user_1.follow(user_2)

print(f"Followers: {user_1.followers}")
print(f"Following: {user_1.following}")
print(f"Followers: {user_2.followers}")
print(f"Following: {user_2.following}")











# def create_user(usuario):
# # usuario
#     usuario = User(int(input("Enter the Id: ")), input("Enter the username: "))
#     print(f"{usuario.id}\n{usuario.username}")
# create_user(usuario="User1")
# create_user(usuario="User2")
# create_user(usuario="User3")
# print(use)
# print(user_1.username)

