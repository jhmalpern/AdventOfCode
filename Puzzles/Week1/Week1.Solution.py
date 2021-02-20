#!/usr/bin/python3

#Imports
import time 
import re



def main():
    
    #Start Time
    startTime = time.time()

    # Step 1: Read in .txt file
    # Step 2: Use regular expressions to create list of occurences of '(' and ')'
    # Step 3: Find difference in length of those lists
    with open('PuzzleString.txt','r') as f:
        puzzleInput = f.read()
    up = ([i for i in range(len(puzzleInput)) if puzzleInput.startswith('(',i)])
    down = ([i for i in range(len(puzzleInput)) if puzzleInput.startswith(')',i)])
    print(len(up)-len(down))
    print("It took %s to execute this solution" % (round(time.time()-startTime, 4)))

if __name__ == "__main__":
    main()