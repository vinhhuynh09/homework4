import time  # used for time.ctime()

def timestamp(func):
    def wrapper():
        currentTime = time.ctime()  # stores current time as a string
        print(currentTime)
        func()
    return wrapper

from log import timestamp

@timestamp
def hi():
    print('hi')

def main():
    hi()

if __name__ == "__main__":
    main()
