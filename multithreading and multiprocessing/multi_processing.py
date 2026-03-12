# Multiprocessing 
# It allows you to create processes that run in parallel
# When to use?
# 1. CPU-Bound Tasks - tasks that are heavy for CPU uses (Mathematical computation, data processing).
# 2. Parallel execution - Using multiple cores of CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'square {i*i}')

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube {i*i**i}")

if __name__ == "__main__":

    # create 2 processes
    p1 = multiprocessing.Process(target = square_numbers)
    p2 = multiprocessing.Process(target = cube_numbers)

    t = time.time()
    # start the process
    p1.start()
    p2.start()

    # wait for the process to complete
    p1.join()
    p2.join()

    f_t = time.time() - t
    print(f'Time taken : {f_t}')