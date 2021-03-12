# imports

##### Part 2 #####
with open("PuzzleInput.txt","r") as f:
    puzzleInput = f.read().splitlines()
calc = dict()
signals = dict() #Dictionary of wire signals AFTER operation successful
signals2 = dict()
for line in puzzleInput:
        (oper, res) = line.split("->") #split into operation to get wire, and wire
        calc[res.strip()] = oper.strip().split(' ') # value for key of wire is operations


def find_a(wire):
    try:
        return(int(wire)) #try to return int(wire) but pass if can't b/c value doesn't exist
    except:
        #print(wire)
        pass
    if wire not in signals: # 'a' hasn't been solved yet so need to calculate another wire
        oper = calc[wire]
        if len(oper) == 1: # If it is just an assignment, set wire value equal to itr
            res = find_a(oper[0]) 
        else:
            action = oper[-2] # Identify bitwise operator
            if action == 'AND':
              res = find_a(oper[0]) & find_a(oper[2]) # add two results together...but find recursively
            elif action == 'OR':
              res = find_a(oper[0]) | find_a(oper[2]) # Or result
            elif action == 'NOT': 
              res = ~find_a(oper[1]) & 65535
            elif action == 'RSHIFT':
              res = find_a(oper[0]) >> find_a(oper[2])
            elif action == 'LSHIFT':
              res = find_a(oper[0]) << find_a(oper[2])
        signals[wire] = res
    return int(signals[wire])

def find_a_again(wire):
    try:
        return(int(wire)) 
    except:
      pass
    if wire not in signals2: 
        oper = calc[wire]
        if len(oper) == 1: 
              res = find_a_again(oper[0])
              if wire == 'b':
                res = int(find_a('a'))
        else:
            action = oper[-2] 
            if action == 'AND':
              res = find_a_again(oper[0]) & find_a_again(oper[2]) 
            elif action == 'OR':
              res = find_a_again(oper[0]) | find_a_again(oper[2]) 
            elif action == 'NOT': 
              res = ~find_a_again(oper[1]) & 65535
            elif action == 'RSHIFT':
              res = find_a_again(oper[0]) >> find_a_again(oper[2])
            elif action == 'LSHIFT':
              res = find_a_again(oper[0]) << find_a_again(oper[2])
        signals2[wire] = res
    return signals2[wire]

def main():
    print("The signal at wire 'a' is: %d" % (find_a_again('a')))

if __name__ == "__main__":
    main()