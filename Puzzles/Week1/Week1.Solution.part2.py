#!/usr/bin/python3

#Imports
import time
import re

def main():
    startTime = time.time()

    with open("PuzzleString.txt") as f:
        puzzleInput = f.read()
    
    # Need to figure out when we enter the basement for the FIRST time
    floor=0 #Starts at ground (floor = 0)
    for i in range(len(puzzleInput)):
        floor = floor + 1 if puzzleInput[i] == "(" else  floor-1
        if floor <0: 
            print("Basement reached at turn %s" % (i+1))
            break
    
    print("Code took %s seconds to execute" % round(time.time() - startTime, 4))

if __name__ == "__main__":
    main()