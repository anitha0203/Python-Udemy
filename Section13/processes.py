import time
from multiprocessing import Process


def ask_user():
    start = time.time()
    user_input = input("Enter your name: ")
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start}')


def complex_calculations():
    start = time.time()
    print('Started calculating...')
    [x**2 for x in range(20000000)]
    print(f'complex_calculation, {time.time() - start}')


start = time.time()
ask_user()
complex_calculations()
print(f'Single thread total time: {time.time() - start}')

process = Process(target=complex_calculations)
process.start()

start = time.time()
ask_user()
process.join()

print(f'Two process total time: {time.time() - start}')

