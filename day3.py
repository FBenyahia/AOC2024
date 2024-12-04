import re

from utils import *
s = get_input(3)
ans = 0
pattern = re.compile(r"mul\((\d+),(\d+)\)")
l= re.findall(pattern, s)
for e in l:
    ans+=int(e[0])*int(e[1])
print(ans)

ans=0
lastchar = ""
lastchar2 = ""
isDo = True

for char in s:
    if isDo:
        if lastchar[-7:]=="don't()":
            isDo = False
            lastchar+=" "
        else:
            lastchar+=char
    else:
        lastchar2+=char
        if lastchar2[-4:]=="do()":
            isDo=True
pattern = re.compile(r"mul\((\d+),(\d+)\)")
l= re.findall(pattern, lastchar)
for e in l:
    ans+=int(e[0])*int(e[1])
print(ans)