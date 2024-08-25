#THIS IS A INFO-GENERATING HELPER
import random
import sys

alpha = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

# This opens the file in write mode to clear its contents at the start
with open("items.txt", "w") as file:
    file.write("")

def accessbility(argv):
    if len(argv) < 3:
        sys.exit("Not enough command line arguments.")
    else:
        return True

def main():
    results = list()
    for a in range(1, int(sys.argv[1])+1):
        string = ""
        for b in range(1, int(sys.argv[2])+1):
            alphabet = random.choice(alpha)
            string += alphabet
        results.append(string)
        # Write each generated string to the file
        with open("items.txt", 'a') as file:
            file.write(f'{string}\n')

if accessbility(argv=sys.argv):                 
    main()