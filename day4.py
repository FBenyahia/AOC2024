
from utils import *
s = get_input(4)


ans = 0

s = s.splitlines()
for i in range(len(s)):
    for j in range(len(s[0])):
        if s[i][j] == 'X':
            if i>=3 and s[i-1][j]=='M' and s[i-2][j]=='A'and s[i-3][j]=='S':
                ans+=1
            if i>=3 and j<len(s[0])-3 and s[i-1][j+1]=='M' and s[i-2][j+2]=='A'and s[i-3][j+3]=='S':
                ans +=1
            if j<len(s[0])-3 and s[i][j+1]=='M' and s[i][j+2]=='A'and s[i][j+3]=='S':
                ans +=1
            if i<len(s)-3 and j<len(s[0])-3 and s[i+1][j+1]=='M' and s[i+2][j+2]=='A'and s[i+3][j+3]=='S':
                ans +=1
            if i<len(s)-3 and s[i+1][j]=='M' and s[i+2][j]=='A'and s[i+3][j]=='S':
                ans +=1
            if i<len(s)-3 and j>=3 and s[i+1][j-1]=='M' and s[i+2][j-2]=='A'and s[i+3][j-3]=='S':
                ans +=1
            if  j>=3 and s[i][j-1]=='M' and s[i][j-2]=='A'and s[i][j-3]=='S':
                ans +=1
            if  i>=3 and j>=3 and s[i-1][j-1]=='M' and s[i-2][j-2]=='A'and s[i-3][j-3]=='S':
                ans +=1

print(ans)
ans=0

for i in range(len(s)):
    for j in range(len(s[0])):
        if s[i][j] == 'A':
            if i>=1 and i<len(s)-1 and j>=1 and j<len(s[0])-1 and s[i-1][j+1]=='M' and s[i+1][j-1]=='S':
                if (s[i-1][j-1]=='M' and s[i+1][j+1]=='S') or (s[i+1][j+1]=='M' and s[i-1][j-1]=='S'):
                    ans +=1
            if i>=1 and i<len(s)-1 and j>=1 and j<len(s[0])-1  and s[i+1][j+1]=='M' and s[i-1][j-1]=='S':
                if (s[i-1][j+1]=='M' and s[i+1][j-1]=='S') or (s[i+1][j-1]=='M' and s[i-1][j+1]=='S'):
                    ans +=1
            if i>=1 and i<len(s)-1 and j>=1 and j<len(s[0])-1  and s[i+1][j-1]=='M' and s[i-1][j+1]=='S':
                if (s[i-1][j-1]=='M' and s[i+1][j+1]=='S') or (s[i+1][j+1]=='M' and s[i-1][j-1]=='S'):
                    ans +=1
            if i>=1 and i<len(s)-1 and j>=1 and j<len(s[0])-1  and s[i-1][j-1]=='M' and s[i+1][j+1]=='S':
                if (s[i-1][j+1]=='M' and s[i+1][j-1]=='S') or (s[i+1][j-1]=='M' and s[i-1][j+1]=='S'):
                    ans +=1
print(ans/2)