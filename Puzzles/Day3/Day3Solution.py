#!/usr/bin/python3

import time
from collections import Counter #Can use Counter to count the number of unique elements in a list

def main():
    
    startTime = time.time()
    
    with open("PuzzleInput.txt") as f:
        puzzleInput = f.read()
    
    
    x, y = [0,0]
    location = x, y
    house = []
    house.append(location) # Santa starts at the first location
    
    ##### PART 1 #####
    for i in range(len(puzzleInput)):
        if puzzleInput[i] == ">":
            x +=1
        elif puzzleInput[i] == "^":
            y +=1
        elif puzzleInput[i] == "<":
            x = x-1
        else:
            y = y-1
        location = x, y
        house.append(location)
    a = len(Counter(house).keys()) # Counts unique homes
    
    print("Solution to PART 1: \n There are %s homes that were visited at least once \n This solution took %s seconds" % (a,round(time.time() - startTime, 4)))

    house = []

    ##### PART 2 #####
    startTime = time.time()

    s1x, s1y = [0,0]
    s2x, s2y = [0,0]
    location = s1x, s1y
    house.append(location) # santa starts at the first location

    for i in range(len(puzzleInput)):
        if (i % 2 == 0):
            if puzzleInput[i] == ">":
                s1x +=1
            elif puzzleInput[i] == "^":
                s1y +=1
            elif puzzleInput[i] == "<":
                s1x = s1x-1
            else:
                s1y = s1y-1
            location = s1x, s1y
        else:
            if puzzleInput[i] == ">":
                s2x +=1
            elif puzzleInput[i] == "^":
                s2y +=1
            elif puzzleInput[i] == "<":
                s2x = s2x-1
            else:
                s2y = s2y-1
            location = s2x, s2y
        house.append(location)
    a = len(Counter(house).keys()) # Counts unique homes
    print("Solution to PART 2: \n There are %s homes that were visited at least once \n This solution took %s seconds" % (a,round(time.time() - startTime, 4)))
    
if __name__ == "__main__":
    main()