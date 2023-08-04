def starts_with_r(friend):
    return friend.startswith('A')


friends = ['Anitha', 'Anu', 'Sri']
starts_with_r = filter(starts_with_r, friends)

print(list(starts_with_r))



#               ORRERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR


starts_with_r = filter(lambda x: x.startswith('A'), friends)

print(list(starts_with_r))



#               ORRERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR

another_starts_with = (f for f in friends if f.startswith('A'))

print(next(another_starts_with))
print(list(another_starts_with))
