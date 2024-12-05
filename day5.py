from utils import *
s = get_input(5)
s = s.splitlines()

#Really bad complexity but work well
#Be carefull, I splitted the file in two for parsing issue

ans=0
with open("inputs/day5_2.txt") as f:
    for line in f:
        print(line)
        line = line.split(',')
        line[-1] = line[-1][:-1]
        line = [int(line[i]) for i in range(len(line))]
        for i in range(len(s)):
            isOkay = True
            for rule in s:
                rule = rule.split('|')
                rule = [int(rule[i]) for i in range(len(rule))]
                if rule[0] in line and rule[1] in line:
                    if line.index(rule[0]) > line.index(rule[1]):
                        isOkay = False
        if isOkay:
            ans+=line[int((len(line))/2)]



print(ans)

with open("inputs/day5_2.txt") as f:
    for line in f:
        print(line)
        line = line.split(',')
        if line[-1] == '\n':
            line[-1] = line[-1][:-1]
        line = [int(line[i]) for i in range(len(line))]
        isOkay = True
        for i in range(len(s)):
            for rule in s:
                rule = rule.split('|')
                rule = [int(rule[i]) for i in range(len(rule))]
                if rule[0] in line and rule[1] in line:
                    i1 =line.index(rule[0])
                    i2 = line.index(rule[1])
                    if i1 > i2:
                        isOkay = False
                        line[i1], line[i2] = line[i2], line[i1]  
        if not isOkay:
            ans+=line[int((len(line))/2)]
            

print(ans)