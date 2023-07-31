''' first example
def start_end_decorator(func): 

    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        func()
        print('End')
        return result
    return wrapper

@start_end_decorator
def print_name():
    print('Dmitry')
def add5(x):
    return x + 5
# print_name = start_end_decorator(print_name) #do the same things like @start_end_decorator

print_name()
result = add5(10)
print(result)
'''
'''
def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def add15(x):
    return x + 15
# print_name = start_end_decorator(print_name) #do the same things like @start_end_decorator

result = add15(10)
print(result)
'''
'''
import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something...
        result = func(*args, **kwargs)
        # Do something afterwords
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5
# print_name = start_end_decorator(print_name) #do the same things like @start_end_decorator
'''
