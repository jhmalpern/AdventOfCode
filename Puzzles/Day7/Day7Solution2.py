import time

calc = dict()
results = dict()


with open("PuzzleInput.txt","r") as f:
        commands = f.read().splitlines()

startTime = time.time()
for command in commands:
    (ops, res) = command.split('->')
    calc[res.strip()] = ops.strip().split(' ')

def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass
    #print(results)

    if name not in results:
        ops = calc[name]
        print(ops)
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
              res = calculate(ops[0]) & calculate(ops[2])
            elif op == 'OR':
              res = calculate(ops[0]) | calculate(ops[2])
            elif op == 'NOT':
              res = ~calculate(ops[1]) & 0xffff
            elif op == 'RSHIFT':
              res = calculate(ops[0]) >> calculate(ops[2])
            elif op == 'LSHIFT':
              res = calculate(ops[0]) << calculate(ops[2])
        results[name] = res
    return results[name]


print("a: %d" % (calculate('a')))
print("This solution took %s seconds" % (round(time.time()-startTime, 4)))