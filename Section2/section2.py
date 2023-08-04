# numbers = [3, 5, 6, 7, 2]

# num = int(input("Enter number: "))

# if (num%2) == 0:
#   print("Even number")
# else:
#   print("Odd number")




# friends = ["Anitha", "Ani", "Anu"]
# family = ["Sri", "Rani", "Srinu"]

# name = input("Enter your name: ")

# if name in friends:
#   print("Hello, friend")
# elif name in family:
#   print("Hello, family")
# else:
#   print("Idon't know u")













# i=0
# while i<5:
#   print("*")
#   i+=1


# print("Exercise")
# user_input = input("Enter menu: ")


# while user_input:
#     if user_input == 'p':
#         print("Hello")
#         user_input = input("Enter menu: ")
#     elif user_input == 'q':
#         user_input = False
#     else:
#         user_input = input("Enter menu: ")

















# numbers = [3, 5, 6, 7, 2]

# for num in numbers:
#   print(num)

# for i in range(10):
#   print("*")


# for i in range(2, 20, 3):            #        (start, end, difference)
#   print(i)                        #    2 5 8 11 14 17



# friends = [("Anitha", 21), ("Anu", 22)]

# for name, age in friends:
#   print(name, age)
# print()

# for friend in friends:
#   name, age = friend
#   print(name, age)
# print()

# for friend in friends:
#   name = friend[0]
#   age = friend[1]
#   print(name, age)
# print()








# for i in range(100):
#     if (i+1)%3 == 0 and (i+1)%5 == 0:
#         print("FizzBuzz")
#     elif (i+1)%3 == 0:
#         print("Fizz")
#     elif (i+1)%5 == 0:
#         print("Buzz")
#     else:
#         print(i+1)


            #      exercise

# for i in range(1, 101):
#     if i%3 == 0 and i%5 == 0:
#         print("FizzBuzz")
#     elif i%3 == 0:
#         print("Fizz")
#     elif i%5 == 0:
#         print("Buzz")
#     else:
#         print(i)











# cars = ["ok", "ok", "ok", "ok", "faulty"]

# for car in cars:
#   if car != "ok":
#     print("The car has some fault")
#     break
#   print("the car is awesome")
# else:
#   print("Every car is awesome")


#                       #    prime number checking
# for i in range(2, 10):
#   if 10%i == 0:
#     print("the number is not prime number")
#     break
# else:
#   print("the given number is prime number")



#                       #  slice


# cars = ["ani", "ok", "kk", "okay", "faulty"]

# print(cars[:4])                 #  ['ani', 'ok', 'kk', 'okay']

# print(cars[2:4])                # ['kk', 'okay']

# print(cars[-3:])                # ['kk', 'okay', 'faulty']

# print(cars[:-2])                # ['ani', 'ok', 'kk']

# print(cars[-3:-1])              # ['kk', 'okay']






# numbers = [0, 1, 2, 3, 4]

#         # number1 = []
        
#         # for num in numbers:
#         #   number1.append(num * 2)
#         # print(number1)

#               ###############        OR

#         # number1 = [number * 2 for number in numbers]
#         # print(number1)

# ages = [22, 21, 23, 24]
# age_str  = [age for age in ages]
# # age_str  = [f"My friend is {age} old" for age in ages]

# print(age_str)


# ages = [22, 21, 23, 24]
# odds  = [age for age in ages if age % 2 ==1]
# # age_str  = [f"My friend is {age} old" for age in ages]

# print(odds)


# friends = ["Anitha", "Ani", "Anu"]
# time = [3, 5, 4]

# list = {
#   friends[i] : time[i] for i in range(len(friends)) if time[i] > 3
# }

# print(list)


# friends = ["Anitha", "Ani", "Anu"]
# time = [3, 5, 4]


# # list = {
# #   friends[i] : time[i] for i in range(len(friends)) 
# # }

# list = dict(zip(friends, time))

# print(list)



# # enumerate

# friends = ["Anitha", "Ani", "Anu"]

# for c, f in enumerate(friends, start=1):
#   print(c, f)


# data = dict(enumerate(friends))
# print(data)

# # ORRRRRRRRRRRRRRRRRRRRRR

# print(dict(zip([0,1,2], friends)))

# # ORRRRRRRRRRRRRRRRRRRRRR

# data = dict(enumerate(friends))
# print(data)











# print("exercise")


import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

top_player = players[0]  

for player in players:  
    matched_numbers = len(player["numbers"].intersection(lottery_numbers))  
    if matched_numbers > len(top_player["numbers"].intersection(lottery_numbers)):  
        top_player = player  
 

winnings = 100 ** len(top_player["numbers"].intersection(lottery_numbers))
 
print(f"{top_player['name']} won {winnings}.")














def sum1(a, b, f):
  print("function", a+b)
  print(f)

friends = ["Anitha", "Ani", "Anu"]
sum1(2,3, friends)



print(1, 2, 3, 4, sep=" - ")

yy = 3

def add(x=7, y=yy):
  print(x+y)

add(3)


divide = lambda x, y: x/y

print(divide(2,2))

def age(d, g):
  print(g(d))
  return g(d) >= 18

user = {"username": "anitha", "age": "35"}

print(age(user, lambda x: int(x['age'])))