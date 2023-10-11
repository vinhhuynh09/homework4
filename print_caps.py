def allcaps(func):
    def wrapper():
        capitalizedResult  = func()
        return capitalizedResult .upper()
    return wrapper

