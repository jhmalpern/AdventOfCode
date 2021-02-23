#!/usr/bin/python3
import time

def main():
    startTime = time.time()
    with open("PuzzleInput.txt",'r') as f:
        puzzleInput = f.read().splitlines()    

    #####   PART 1   #####
    #For Loop approach
    wrapNeeded = 0
    for i  in range(len(puzzleInput)):
        side1 = int(puzzleInput[i].split('x')[0]) * int(puzzleInput[i].split('x')[1])
        side2 = int(puzzleInput[i].split('x')[1]) * int(puzzleInput[i].split('x')[2])
        side3 = int(puzzleInput[i].split('x')[0] )* int(puzzleInput[i].split('x')[2])
        slack = min(side1,side2,side3)
        wrapNeeded = wrapNeeded + (2*side1) + (2*side2) + (2*side3) + slack  


    print("Elves need %s feet of wrapping paper" % (wrapNeeded))
    print("It took %s to execute this solution" % (round(time.time()-startTime, 4)))

if __name__ == "__main__":
    main()
