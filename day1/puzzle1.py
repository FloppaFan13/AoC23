import math

inputFile = open('input.txt', "r")
lines = inputFile.readlines()

count = 0
total = 0

numbers = []

# First loop
for line in lines:
    lString = line.strip()
    tempHold = []
    for char in lString:
        if char.isnumeric():
            tempHold.append(char)
    if len(tempHold) > 1:
        print(tempHold, "#")
        numbers.append(int(str(tempHold[0]) + str(tempHold[-1])))
    elif len(tempHold) == 1:
        numbers.append(int(str(tempHold[0] + str(tempHold[0]))))
    
for x in range(len(numbers)):
    total += numbers[x];

print(total)