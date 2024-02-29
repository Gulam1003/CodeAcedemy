"""Write a decorator that decorates a string-returning function in an email style.
 For example: write_email("this is some text") should return
"To whom it may concern,
this is some text
Sincerely,
Sender"""

def decoratorFunction(func):
    def wrapper(text):

        print("To whom it may concern,")
        func(text)
        print(f"Sincerely, Sender {text}")
    return wrapper

@decoratorFunction
def textfunction(name):
    print("How are you")


textfunction("Gulam")
