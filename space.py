def remove_trailing_whitespace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs).strip()
        return result
    return wrapper

def replace_spaces_with_underscores(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs).replace(' ', '_')
        return result
    return wrapper

def convert_to_lowercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs).lower()
        return result
    return wrapper


@replace_spaces_with_underscores
@convert_to_lowercase
@remove_trailing_whitespace
def prompt_user_input():
    user_input = input("Enter you string: ")
    return user_input

cleaned_text = prompt_user_input()
print(cleaned_text)
