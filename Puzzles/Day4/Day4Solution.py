import hashlib 
import time

def main():

    with open('PuzzleInput.txt', 'r') as f:
        puzzleInput = f.read()
    #puzzleInput = 'abcdef'
    

    ##### Part 1 #####
    startTime = time.time()
    i=0
    while True or i < 5000000: 
        i +=1
        h = hashlib.md5((puzzleInput + str(i)).encode()).hexdigest()
        if h.startswith('00000'):
            print("Finished on iter %s and took %s seconds" % (i, time.time()-startTime))
            break
    
    ##### Part 2 #####

    startTime = time.time()
    i=0
    while True or i < 5000000: 
        i +=1
        h = hashlib.md5((puzzleInput + str(i)).encode()).hexdigest()
        if h.startswith('000000'):
            print("Finished on iter %s and took %s seconds" % (i, time.time()-startTime))
            break        

if __name__ == "__main__":
    main()