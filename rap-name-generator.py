# Guided Exploration No. 3
# Jacob Clement

# Imports the random library
import random

# Creates an empty list of possible names
possible_names = []

# Opens a text file that can be written to
outputFile = open('rap-names-output.txt', 'w')

# Opens the file to read and assigns a handle, also this allows us to do stuff with the file
with open('rap-names.txt', 'r') as dataFile:
    # Loops through all the names in the rap-names file and appends them to a list
    for name in dataFile:
        possible_names.append(name.rstrip())

# Gets the number of rap names and the amount of parts from the user
count = int(input('How many rap names would you like to create? '))
parts = int(input('How many parts should the name contain? '))

# Loops witht the amount of names the user wants
for i in range(count):
    # Creates an empty list for name parts
    name_parts = []
    # Loops with the amount of parts the user watned
    for j in range(parts):
        # Appends each part by generating a random number in between 0 and the amount
        # of possible names  and picking a random part in that range
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

# Writes the rap name to the output text file by joining the name parts together
# from theh list
outputFile.write(f"{' '.join(name_parts)}\n")
# Prints the name parts to the user
print(f"{' '.join(name_parts)}")

# Closes the output file
outputFile.close()
