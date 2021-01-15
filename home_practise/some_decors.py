import time

def cache_decor(function):
    holder = dict()
    def cache_storage(*args):
        nonlocal holder
        result = function(*args)
        if args not in holder.keys():
            holder[args] = result
        print(holder)
        return result

    return cache_storage


def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        time_now = time.time()
        result = func(*args, **kwargs)
        finish_time = time.time() - time_now
        print(finish_time)
        return result
    return wrapper

def exception_handler_decorator(exception_type=Exception, max_retries=1):
    def wrapper(func):

            def recersive_call(*args, **kwargs):
                result = None
                for one_try in range(max_retries):
                    try:
                        result = func(*args, **kwargs)
                    except Exception as e:
                        print(f'Catched {e} in {one_try+1} try')
                    else:
                        break

                return result

            return recersive_call
    return wrapper



@exception_handler_decorator(Exception,2)
def funcy_broken():
    return 1 - "1"



@timeit_decorator
def num_in_degree(num,deg):
    lister = []
    time.sleep(3)
    for i in range(1,deg):
         lister.append(num**i)
    return lister

@cache_decor
def adder(num1, num2):
    return num1+num2,

for i,j in enumerate(range(5,10)):
    print(adder(i,j))

#print(num_in_degree(125, 17))
#print(funcy_broken())

