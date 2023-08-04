def add_all(a1, a2, a3, a4):
    return a1 + a2 + a3 + a4


vals = (1, 3, 5, 7)

print(add_all(*vals))


vals = {'a1': 1, 'a2': 3, 'a3': 7, 'a4': 5}

print(add_all(**vals))

# print(add_all(a1=vals['a1'], a2=vals['a2'].............))


def add_all(*args):
    return sum(args)


print(add_all(1, 3, 5, 7))


def pretty_print(**kwargs):
    for k, v in kwargs.items():
        print(f'For {k} we have {v}.')


pretty_print(username='Anitha', access_level="admin")

pretty_print(**{'username': 'Anitha', 'access_level': "admin"})
