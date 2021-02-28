#!/usr/bin/python3
import time

def main():
    startTime = time.time()
    #with open("PuzzleInput.txt",'r') as f:
    #    puzzleInput = f.read().splitlines()    

    #####   PART 1   #####
    benchTime = []
    for j in range(1000):
        startTime = time.time()
        with open("PuzzleInput.txt",'r') as f:
            puzzleInput = f.read().splitlines() 
        wrapNeeded = 0
        for i  in range(len(puzzleInput)):
            l, w, h = [int(i) for i in puzzleInput[i].split('x')]
            area = 2*l*w + 2*w*h + 2*l*h
            wrapNeeded = wrapNeeded + area + min(l*w,w*h,l*h)
        benchTime.append(time.time()-startTime)
    print("Elves need %s feet of wrapping paper" % (wrapNeeded))
    print("On average, it took %s seconds to complete Part1" % (sum(benchTime)/len(benchTime)))

    #####   PART 2   #####
    benchTime2 = []
    for j in range(1000):
        startTime = time.time()
        with open("PuzzleInput.txt",'r') as f:
            puzzleInput = f.read().splitlines() 
        bow = 0
        wrap = 0
        for i in range(len(puzzleInput)):
            l, w, h = [int(i) for i in puzzleInput[i].split('x')]
            bow = (l*w*h)
            wrap = wrap + bow + min(2*(l+h), 2*(l+w), 2*(w+h))
        benchTime2.append(time.time()-startTime)

    print("Elves need %s feet of ribbon" % (wrap))
    print("On average, it took %s seconds to complete Part2" % (sum(benchTime2)/len(benchTime2)))


if __name__ == "__main__":
    main()
