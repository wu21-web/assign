import random

def info():
    min = input("[MIN]:\n")
    max = input("[MAX]:\n")

    min = int(min)
    max = int(max)

    numbers = range(min, max + 1)
    return tuple(numbers)

def keys():
    items = list()
    try:
        with open("items.txt", mode='r') as file:
            content = file.read().splitlines()  # Read lines instead of characters
            for i in content:
                item = (i, None)  # Use tuple to preserve pairing
                items.append(item)  # Corrected indentation
    except FileNotFoundError:
        exit("You need to provide a set of items in a file called 'items.txt' you want to pair. For example:\njohn\nlisa")
    return items

def accessbility(a, b):
    if len(a) == len(b):
        return True
    else:
        return False
    
def randomize(options, pairing):
    results = list()
    options = list(options)  # Convert tuple to list
    while options:
        c = random.choice(options)
        options.remove(c)  # Now works because options is a list

        choice = random.choice(pairing)
        pairing.remove(choice)  # Simplified deletion

        cache = (c, choice[0])  # Use tuple to store the pair
        results.append(cache)

    return results
    