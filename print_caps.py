def allcaps(func):
    def wrapper():
        result = func()    # result equals what is returned in greet()
        capitalizedResult = result.upper()
        print(capitalizedResult)

    return wrapper

from print_caps import allcaps  # import allcaps decorator

@allcaps
def greet(): # greet() is decorated with @allcaps so wrapper() inside allcaps gets executed with func being greet()
    return "hello World!"

def main():
    greet()  # calls greet()
