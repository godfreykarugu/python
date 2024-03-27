import random

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# # print("name")
# print(name)
# print("Your age is:" +age)
#
# # for i in range(10):
# #     print(i  )
#
# print(f"Your name is {name} and your age is {age}")

# def roll():
#     max_value = 6
#     min_value = 1
#     return random.randint(min_value, max_value)
# value = roll()
# print(value)

# import random
#
# x = random.randint(1,10)
#
while True:
    players = input("Enter number of players: ")
    if players.isdigit():
        player= int(players)
        if 0 < player <=4:
            break
    else:
        print("Enter a valid number")


