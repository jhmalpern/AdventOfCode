#!/usr/bin/python3

import time
from collections import Counter #Can use Counter to count the number of unique elements in a list

def main():
    
    startTime = time.time()
    
    with open("PuzzleInput.txt") as f:
        puzzleInput = f.read()
    
    x, y = [0,0]
    
    print(puzzleInput[0])
    location = []
    house = []
    
    #locX = [x+1 if puzzleInput[i] == ">" else x-1 for i in range(len(puzzleInput))]
    ##### PART 1 #####
    for i in range(len(puzzleInput)):
        #x = [x+1 if puzzleInput[i] == ">" else x-1 if puzzleInput[i] == "<" for i in len(puzzleInput)]
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
    a = print(len(Counter(house).keys())+1) # Counts unique homes...need to add +1 b/c gives home at starting location
    
    # multiple={k:v for (k,v) in visits.items() if v > 0} # Identified elements of counts that are greater than 1
    print("There are %s homes that were visited more than once" % (a))
    
    print("Day3 Solution PART 1 took %s seconds" % (round(time.time() - startTime, 4)))

if __name__ == "__main__":
    main()