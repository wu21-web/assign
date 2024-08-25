import func

numbers = func.info()
items = func.keys()

if func.accessbility(numbers, items):
    for i in func.randomize(numbers, items):
        print(f"\n{i}")
else:
    exit("You do not have enough chosen items or numbers.")