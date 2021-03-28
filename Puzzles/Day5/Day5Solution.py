# Imports
import time
from re import search

# From https://www.geeksforgeeks.org/python-count-display-vowels-string/
# Counts and returns number of vowels in a string

##### Part 1 functions #####
def Check_Vow(string, vowels):
    final = [each for each in string if each in vowels]
    return(len(final))

def Check_repeat(string):
    for each in range(1,len(string)):
        if(string[each] == string[each-1]):
            return(True)

def Check_bad(string, test_list):
    res = [each for each in test_list if each in string]
    if len(res) >=1 :
        return(True)

##### Part 2 functions #####

def Check_doublet(string):
    doublet = []
    for each in range(len(string)):
        try:
            doublet.append(string[each] + string[each + 1])
        except:
            repeats = [doublet[dub] for dub in range(len(doublet)) if doublet[dub] in doublet[dub + 2:len(doublet)]]
    return(repeats)
    #return(doublet)


def Check_sandwich(string):
    for each in range(len(string)):
        try:
            if string[each] == string[each + 2]:
                return(True)
        except:
            pass


##### Main #####

def main():
    with open("PuzzleInput.txt","r") as f:
        puzzleInput = f.read().splitlines()
    
    ##### Part 1 #####
    
    startTime1 = time.time()
    vowels = "aeiou"
    bad = ["ab", "cd", "pq", "xy"]
    niceString = 0

    for i in range(len(puzzleInput)):
        if Check_Vow(puzzleInput[i],vowels) >= 3 and Check_repeat(puzzleInput[i]) and not Check_bad(puzzleInput[i],bad): # If it has more than 2 vowels
            niceString +=1
    endTime1 = time.time()

    ##### Part 2 #####

    startTime2 = time.time()
    
    niceString2 = 0
    for i in range(len(puzzleInput)):
        if Check_sandwich(puzzleInput[i]) and len(Check_doublet(puzzleInput[i]))>0:
            niceString2 += 1
    endTime2 = time.time()


    ##### Calls #####

    print("There are %s nice strings in Part1:\t" % (niceString))
    print("This solution took %s seconds" % (round(endTime1-startTime1,4)))
    
    print("There are %s nice strings in Part2:\t" % (niceString2))
    print("This solution took %s seconds" % (round(endTime2-startTime2,4)))



if __name__ == "__main__":
    main()