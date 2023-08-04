def numbers():
    i = 0
    while i < 100:
        yield i
        i += 1


g = numbers()
print(next(g))
print(next(g))
print(list(g))

print([x * 2 for x in numbers()])

#
# class FirstHundredGenerator:
#     def __init__(self):
#         self.number = 0
#
#     def __next__(self):
#         if self.number < 100:
#             current = self.number
#             self.number += 1
#             return current
#         else:
#             raise StopIteration()
#
#
# my_gen = FirstHundredGenerator()
# print(next(my_gen))
# print(next(my_gen))
#
#
# # class FirstFiveIterator:
# #     def __init__(self):
# #         self.numbers = [1, 2, 3, 4, 5]
# #         self.k = 0
# #
# #     def __next__(self):
# #         if self.k < len(self.numbers):
# #             return self.numbers[self.k]
# #         else:
# #             raise StopIteration()
# #
# #
# # ggg = FirstFiveIterator()
# #
# # print(next(ggg))
#
# class FirstHundredIterable:
#     def __iter__(self):
#         return FirstHundredGenerator()


class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self


for i in FirstHundredGenerator():
    print(i)

print(sum(FirstHundredGenerator()))


class AnotherIterable:
    def __init__(self):
        self.cars = ['BMW', 'Odi']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


for car in AnotherIterable():
    print(car)


my_numbers = [x for x in [1, 2, 3, 4, 5]]
my_number_gen = (x for x in [1, 2, 3, 4, 5])                # this is not a tuple

print(next(my_number_gen))              #   1
print(next(my_number_gen))              #   2