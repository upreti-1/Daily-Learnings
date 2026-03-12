'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, involve significant computational work. Multiprocessing can be used to distribute the workload across 
multiple CPU cores, improving performance
'''

import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# creating our function to compute the factorial of a given number
def factorial(number):
    result = math.factorial(number)
    print(f'Factorial of {number} is : {result}')
    return result

if __name__ == '__main__':
    numbers = [5000, 6000, 7000, 8000]

    start = time.time()

    # creating a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)

    end = time.time()
    print(f'Results = {results}')
    print(f'Time : {end - start}')