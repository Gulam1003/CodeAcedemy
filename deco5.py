"""
Write a decorator that allows you to pass only string parameters to a function.
"""
def limiter(func):
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, str) for arg in args) or not all(isinstance(value, str) for value in kwargs.values()):
            raise ValueError("Given arguments is not string")
        return func(*args, **kwargs)
    return wrapper

@limiter
def add(a, b, c):
    result = a + b + c
    return result

@limiter
def add1(a, b):
    result = a + b
    return result

print(add1("Gulam", " Ansari"))
print(add(2, 3, 4))
