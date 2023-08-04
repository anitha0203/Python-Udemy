names = input("Enter 3 names: ")
names = set(names.split(' '))
print(names)


people = open('people.txt', 'r')
# peoples = set(people.read().split('\n'))

#           ORRRRRRRRRRRRRRRRRRRRRRRR

peoples = [line.strip() for line in people.readlines()]
peoples = set(peoples)

print(peoples)

nearby = peoples.intersection(names)
print(nearby)

file = open('nearby_people.txt', 'w')

for name in nearby:
    file.write(f'{name} ')

file.close()

