# import time
# from concurrent.futures import ThreadPoolExecutor
#
#
# def ask_user():
#     start = time.time()
#     user_input = input('Enter your name: ')
#     greet = f'Hello, {user_input}'
#     print(greet)
#     print('ask_user: ', time.time() - start)
#
#
# def complex_calculation():
#     print('Started calculating...')
#     start = time.time()
#     [x**2 for x in range(20000000)]
#     print('complex_calculation: ', time.time() - start)
#
#
# start = time.time()
# ask_user()
# complex_calculation()
# print('Single thread total time: ', time.time() - start, '\n\n')
#
# start = time.time()
#
# with ThreadPoolExecutor(max_workers=2) as pool:
#     pool.submit(complex_calculation)
#     pool.submit(ask_user)
#
# print('Two thread total time: ', time.time() - start)

import time
from threading import Thread


def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print('ask_user: ', time.time() - start)


def complex_calculation():
    print('Started calculating...')
    start = time.time()
    [x**2 for x in range(20000000)]
    print('complex_calculation: ', time.time() - start)


# With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')


thread = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()

thread.start()
thread2.start()

thread.join()
thread2.join()

print('Two thread total time: ', time.time() - start)


