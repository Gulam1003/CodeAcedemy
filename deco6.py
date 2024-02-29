"""
Write a python decorator that would return whether the result of a function is even or uneven.
Make sure it works for arbitrary inputs.
For example, if you decorate the following function with this decorator: sum_two_numbers(1, 2)we will get (3, 'odd')
"""

def eo_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result % 2 == 0:
            output = 'even'
        else:
            output = 'odd'
        return result, output
    return wrapper

@eo_decorator
def sum(a, b):
    return a + b

result, output = sum(1, 2)
print(result, output)
