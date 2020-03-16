import functools
import time
import random

PRIMES_LIMIT = 5000

def timer(func):
    """Prints the runtime of the decorated function."""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()

        try:
            value = func(*args, **kwargs)
        except BaseException as error:
            print(f'{type(error).__name__} was caught')
            raise error
        else:
            print(f'Successful test case for number {number}')
        finally:
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Finished {func.__name__!r} in {run_time:.4f} secs")

        if not value:
            return 'Sorry, but your number does`t have any prime numbers!'
        return value
    return wrapper_timer


class Too_much_primes_error(BaseException):
    def __init__(self, number):
        self.number = number
        super().__init__(f'Sorry, but number {self.number} is too large')


@timer
def primes_adder(range_number):
    primes = []
    time.sleep(random.uniform(0.1, 1.0))
    range_number = int(range_number)
    for num in range(range_number):
        if num > 1:
            for i in range(2, (num // 2) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
                if len(primes) > PRIMES_LIMIT:
                    print('Prime numbers:', *primes)
                    raise Too_much_primes_error(number=range_number)
        else:
            continue
    return primes


if __name__ == "__main__":
    print('Hello Mr/Mss!\nThis programs returns all prime numbers in range of inputed your number')
    number = input('Input prime range:\n')
    result = primes_adder(number)
    print('Prime numbers:', *result)

