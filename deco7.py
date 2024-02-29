"""
write a debug decorator that would help you debug function calls.
For example, it should print out the way the function was called,
specifically: take the repr(a) of any positional argument to the function,
all{k}={repr(v)} keyword-value pairs from keyword arguments.
Print out the function name and finally which value the function returned. For example, if I have
@debug
def make_greeting(name, age=None):
     if age is None:
         return f"Howdy {name}!"
     else:
         return f"Whoa {name}! {age} already, you're growing up!"
and then I expect the following output
>>> make_greeting("Benjamin")
Calling make_greeting('Benjamin')
make_greeting() returned 'Howdy Benjamin!'
'Howdy Benjamin!'

"""
def debug(func):
    def wrapper(*args, **kwargs):

        positional_arg = ', '.join([repr(arg) for arg in args] )
        keword_argument = ', '.join([f"{key}={repr(value)}" for key,value in kwargs.items()])
        print(f"calling {func.__name__}({positional_arg}{keword_argument})")
        #print(f"{func.__name__}() returned {positional_arg}{keword_argument} ")
        result = func(*args,**kwargs)
        print(f"{func.__name__}() {result}")
        return result
    return wrapper


@debug
def make_greeting(name, age=None):
     if age is None:
         return f"Howdy {name}!"
     else:
         return f"Whoa {name}! {age} already, you're growing up!"


print(make_greeting("Benjamin",age = 22))