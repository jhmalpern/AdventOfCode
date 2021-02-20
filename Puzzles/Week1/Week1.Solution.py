#!/usr/bin/python3

#Imports
import time 
import re



def main():
    
    #Start Time
    startTime = time.time()

    # Take in String and Return String
    f = open("PuzzleString.txt","r")
    puzzleInput = f.read()
    up = ([i for i in range(len(puzzleInput)) if puzzleInput.startswith('(',i)])
    down = ([i for i in range(len(puzzleInput)) if puzzleInput.startswith(')',i)])
    print(len(up)-len(down))
    print("It took %s to execute this solution" % (round(time.time()-startTime, 4)))
    f.close()

if __name__ == "__main__":
    main()