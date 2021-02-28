#!/usr/bin/python3

#Imports
import time 
import re

def main():
    
    ##### Part 1 #####
    benchTime = []
    for j in range(1000):
        startTime = time.time()

        with open('PuzzleString.txt','r') as f:
            puzzleInput = f.read()

        startTimeRunningTally = time.time()
        floor=0 #Starts at ground (floor = 0)
        for i in range(len(puzzleInput)):
            floor = floor + 1 if puzzleInput[i] == "(" else  floor-1
        benchTime.append(time.time()-startTime)
        
    print("Finished on floor %s" % (floor))
    print("On Average, it took %s seconds to get PART 1 solution" % (sum(benchTime)/len(benchTime)))


    ##### Part 2 #####
    
    benchTime2 = []
    for j in range(1000):

        startTime = time.time()
        with open('PuzzleString.txt','r') as f:
                puzzleInput = f.read()


        floor = 0 #Starts at ground (floor = 0)
        for i in range(len(puzzleInput)):
            floor = floor + 1 if puzzleInput[i] == "(" else  floor-1
            if floor <0: 
                break
        benchTime2.append(time.time()-startTime)
    print("Basement reached at turn %s" % (i+1))
    print("On Average, it took %s seconds to get PART 2 solution" % (sum(benchTime2)/len(benchTime2)))

if __name__ == "__main__":
    main()