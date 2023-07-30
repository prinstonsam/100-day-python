class User:
    def __init__(self, id, user_name):
        self.user_name = user_name
        self.id = id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(id="001", user_name="angela")
user_2 = User(id="002", user_name="Nick")

user_1.follow(user_2)

print(user_1.following)
print(user_2.followers )
