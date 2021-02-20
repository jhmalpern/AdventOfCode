#!/usr/bin/python3

#Imports
import time 
import re



def main():
    
    #Start Time
    startTime = time.time()

    # Step 1: Read in .txt file
    # Step 2: Keep running tally of floor. Much faster than finding the difference at the end
    with open('PuzzleString.txt','r') as f:
        puzzleInput = f.read()

    print("It took %s to execute this solution" % (round(time.time()-startTime, 4)))

    startTimeRunningTally = time.time()
    floor=0 #Starts at ground (floor = 0)
    for i in range(len(puzzleInput)):
        floor = floor + 1 if puzzleInput[i] == "(" else  floor-1
    print("Finished on floor %s" % (floor))

if __name__ == "__main__":
    main()