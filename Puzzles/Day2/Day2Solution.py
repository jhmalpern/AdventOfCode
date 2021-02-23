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
        l, w, h = [int(i) for i in puzzleInput[i].split('x')]
        area = 2*l*w + 2*w*h + 2*l*h
        wrapNeeded = wrapNeeded + area + min(l*w,w*h,l*h)

    print("Elves need %s feet of wrapping paper" % (wrapNeeded))
    print("It took %s to execute this solution" % (round(time.time()-startTime, 4)))

if __name__ == "__main__":
    main()
