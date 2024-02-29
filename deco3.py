"""Write a decorator that decorates a function which only allows to give write numbers (int or float).
Write some functions which work with numbers and test your implementation


def int_checker(func):
    def wrapper(*args):
        new_arg=[]
        for i in args:
            if i is isinstance(int):
                i = i*2
                new_arg.append(i)
                print("made the value twice")

        func(new_arg)

        print("Completed")
    return wrapper()

def add(a,b):
    addition = a+b

add(4,5)"""



def int_checker(func):
    def wrapper(a):
        if not isinstance(a,(int,float)) :
            raise ValueError ("a is not an integer")
        return func(a)
    return wrapper


@int_checker
def function_value(b):
    return b+5


print(function_value(2.5))

















