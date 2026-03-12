# Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(number):
    time.sleep(1)
    return f'Number: {number * number}'

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9,0]

    with ProcessPoolExecutor() as executor:
        results = executor.map(square_numbers, numbers)

    for result in results:
        print(result)
