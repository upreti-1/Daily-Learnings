# MultiThreading
# when to use multithreading ?
#  I/O bound tasks : Tasks that spend more time waiting for I/O operaions (e.g., file operations, network requests)
# concurrent execution : when you want to improve the throughput of application by performing multiple operations concurrently.


import threading

import time

def print_numbers():
    for i in range(5):
        time.sleep(0.5)
        print(f'Number : {i}')

def print_letters():
    for letter in 'abcde':
        time.sleep(0.5)
        print(f'Letter : {letter}')

# creating two threads
t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = print_letters)


t = time.time()
# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()
f_t = time.time() - t
print(f_t)