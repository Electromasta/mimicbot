import random
import re

pattern = ("([0-9]\\d*)*[d]([0-9]\\d*)([+-]\\d+)?")

def main():
    print("Enter Command")
    u = input()
    print(parseDice(u))

def parseDice(x):
    p = re.compile(pattern)
    rolls =  p.match(x).group(1)
    if rolls is None:
        rolls=1
    else:
        rolls = int(rolls)
    sides = int(p.match(x).group(2))
    addition = p.match(x).group(3)
    if addition is None:
        addition=0
    else:
        if addition[:1] == '+':
            addition = int(addition[1:])
        else:
            addition = -int(addition[1:])
    return roll(rolls, sides, addition)

def roll(x, y, z):
    if y>100 or x*y > 241:
        return 'No Thanks'
    
    result = "Rolling: ["
    total = 0;
    
    for x in range(0, x):
        r = random.randrange(1, y)
        total += r
        result += str(r) + ', '

    tail = ''
    if z < 0:
        tail += str(z)
        total += z
    elif z > 0:
        tail += '+' + str(z)
        total += z

    result = result[:-2] + "]" + tail + " = " + str(total)
    return result

main()
