# age = 30
# print(age)

# float_division = 12 / 4
# print(float_division)

# interger_division = 12 // 4
# print(interger_division)

# multiline = """
#       Hello Everyone!

# """

# print(multiline)


# age = 34
# age_as_str = str(age)
# print("You are " + age_as_str)
# print(f"You are {age}")

# name = "Anitha"
# greeting = "Hello {}"
# final_greeting = greeting.format(name)
# print(final_greeting)

# name = "Anu"
# final_greeting = greeting.format(name)
# print(final_greeting)

# name = "Anitha"
# greeting = "Hello {name}"
# final_greeting = greeting.format(name=name)
# print(final_greeting)


# name = input("Enter your name: ")
# print(f"Your name is {name}")

# age = int(input("Enter your age: "))
# print(f"Your name is {age * 2}")







# age = 15 > 14
# print(age) 

# val = 30
# val1 = 0

# age = val or val1
# print(age)

# greeting = "there"
# name = input("Enter your name: (optional) ")

# user_name = name or greeting

# print(f"Hello, {user_name}")



#         lists (noting but arrays)

names = ["Anitha", "Anu", 2]
names.append("Ani")
names.remove(2)

print(len(names))

print(names)



#            tuples

friends = ("Anitha", "Ani")

friends = friends + ("Anu",)

print(friends)
print()

#              Sets


friends = {"Anitha", "Ani"}

friends.add("Anu")

print(friends)

friends.add("Anu")

print(friends)

friends.remove("Ani")

print(friends)


print()

friends = {"Anitha", "Ani"}

family = {"Anitha", "Anu", "Sri"}

#             not common in friends
final = friends.difference(family)
print(final)

#             not common in family
final = family.difference(friends)
print(final)

#             not common in both
final = friends.symmetric_difference(family)
print(final)

#             common in both
final = friends.intersection(family)
print(final)

#             union in both
final = friends.union(family)
print(final)




#            Dictonaries

friends_ages = {"Anitha": 22, "Ani": 21, "Anu": 23}

print(friends_ages["Anitha"])

print(friends_ages)
friends_ages["Sri"] = 20
print(friends_ages)

print()

friends = (
  {"name":"Anitha", "age": 21},
  {"name":"Anu", "age": 23}
)

friends = [("Anitha", 21), ("Anu", 23)]

print(friends)                #     [('Anitha', 21), ('Anu', 23)]
f = dict(friends)
print(f)                      #    {'Anitha': 21, 'Anu': 23}


print()
print()
print("example")

lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""

players = [
    {
        'name': 'Anitha',
        'numbers': {1, 2, 3, 4, 5}
    },
    {
        'name': 'Sri',
        'numbers': {4, 8, 12, 16, 20}
    }
]

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""

print(players[0]['numbers'])
player1 = lottery_numbers.intersection(players[0]['numbers'])

print(f"Player {players[0]['name']} got {len(player1)} numbers right")

player2 = lottery_numbers.intersection(players[1]['numbers'])

print(f"Player {players[1]['name']} got {len(player2)} numbers right")






