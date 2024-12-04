from utils import *

s = get_input(2)

s=s.splitlines()
for i in range(len(s)):
    s[i] = s[i].split(' ')


for i in range(len(s)):
    for j in range(len(s[i])):
        s[i][j] = int(s[i][j])
print(s)

ans = 0

for l in s:
    asc = False
    prev=l[0]
    isOkay = True

    for i in range(1, len(l)):
        if i==1 and l[i]>prev and 1<=abs(l[i]-prev)<=3:
            asc=True
            prev = l[i]
        elif asc and prev<l[i] and 1<=abs(l[i]-prev)<=3:
            prev = l[i]

        elif not asc and prev>l[i] and 1<=abs(l[i]-prev)<=3:
            prev = l[i]
        else:
            isOkay = False
    if isOkay:
        ans+=1

#print(ans)
ans=0

def isSafe(level):
    asc = False
    prev=level[0]
    isOkay = True

    for i in range(1, len(level)):
        if i==1 and level[i]>prev and 1<=abs(level[i]-prev)<=3:
            asc=True
            prev = level[i]
        elif asc and prev<level[i] and 1<=abs(level[i]-prev)<=3:
            prev = level[i]

        elif (not asc) and prev>level[i] and 1<=abs(level[i]-prev)<=3:
            prev = level[i]
        else:
            isOkay = False
    return isOkay


for l in s:
    if isSafe(l):
        ans+=1
        print(f"{l} is safe")
    else:
        i=0
        b=True
        while i<len(l) and b:
            x = l.copy()
            x.pop(i)
            print(f"x: {x}, {isSafe(x)}")
            if isSafe(x):
                ans+=1
                print(f"{l} is safe with errors ({i})")

                b=False
            i+=1
submit(2, ans, 2)
isSafe([8, 6, 4, 1])

