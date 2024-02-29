def limiter(func):
    def wrapper(*args, **kwargs):
        if len(args) + len(kwargs) > 2:
            raise ValueError("Total number of arguments is greater than 2")
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

print(add1(4, 5))
print(add(2, 3, 4))
