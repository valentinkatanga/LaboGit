import random

def say_hello_world():
    print("Hello, World!")

def CheckHighestNumber(highest, lowest):
    if (highest >= lowest):
        return True
    return False

def GuessRandomNumber(number, minimum, maximum):
    if (CheckHighestNumber(maximum, minimum) is False):
        minimum, maximum = maximum, minimum

    guessed_number = random.randint(minimum, maximum)
    
    if guessed_number == number:
        return True
    else:
        return False
    
def PrintCountToTen():
    for i in range(11):
        print(i)


say_hello_world()

print(GuessRandomNumber(2, 1, 5))

PrintCountToTen()