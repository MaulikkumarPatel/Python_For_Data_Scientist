# from prettytable import PrettyTable
# table = PrettyTable()
#
# table.add_column("Pokemon Name", ["Pikachu", "Squirtel", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# print(table)
# table.align = "l"
# print(table)

class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "Maulik")
user2 = User("002", "Jack")
# print(user1.user_id, user1.username)
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
