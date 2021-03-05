# imports
import time
import numpy as np

def main():
    
    with open("PuzzleInput.txt", "r") as f:
        puzzleInput = f.read().splitlines()

    ##### PART 1 #####
    
    startTime = time.time()
    lights = np.zeros((1000,1000), 'int32')

    for line in puzzleInput:
        line = line.split()
        if(line[0] == "toggle"):
            x1, y1 = line[1].split(",")
            x2, y2 = line[3].split(",")
            x1, x2, y1, y2 = int(x1), int(x2)+1, int(y1), int(y2)+1
            lights[x1:x2,y1:y2] = np.where(lights[x1:x2,y1:y2] == 0, 1, 0)
        else:
            x1, y1 = line[2].split(",")
            x2, y2 = line[4].split(",")
            x1, x2, y1, y2 = int(x1), int(x2)+1, int(y1), int(y2)+1 
            if(line[1] == "on"):
                lights[x1:x2,y1:y2] = 1
            else:
                lights[x1:x2,y1:y2] = 0
    print("Solution for part 1 is %s lights \n The solution for Part 1 took %s seconds" %(np.sum(lights),round(time.time()-startTime,4)))
    
    ##### PART 2 #####

    startTime = time.time()
    lights = np.zeros((1000,1000), 'int32')

    for line in puzzleInput:
        line = line.split()
        if(line[0] == "toggle"):
            x1, y1 = line[1].split(",")
            x2, y2 = line[3].split(",")
            x1, x2, y1, y2 = int(x1), int(x2)+1, int(y1), int(y2)+1
            lights[x1:x2,y1:y2] = lights[x1:x2,y1:y2] + 2
        else:
            x1, y1 = line[2].split(",")
            x2, y2 = line[4].split(",")
            x1, x2, y1, y2 = int(x1), int(x2)+1, int(y1), int(y2)+1 
            if(line[1] == "on"):
                lights[x1:x2,y1:y2] = lights[x1:x2,y1:y2] + 1
            else:
                lights[x1:x2,y1:y2] = np.where(lights[x1:x2,y1:y2] > 0, lights[x1:x2,y1:y2]-1, 0)
    print("Solution for Part 2 is %s brightness \n The solution for Part 2 took %s seconds" %(np.sum(lights),round(time.time()-startTime,4)))







if __name__ == "__main__":
    main()