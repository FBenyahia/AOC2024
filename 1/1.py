l1 = []
l2 = []
with open("input.txt", 'r') as f:
    for line in f:
        print(line)
        line = line.split('  ')
        line[1] = line[1][1:-1]
        l1.append(int(line[0]))
        l2.append(int(line[1]))
k = 0
l1.sort()
l2.sort()
for i in range(len(l1)):
    k+= abs(l1[i] - l2[i])

print(k)


#Part 2

l1 = []
l2 = []

with open("input.txt", 'r') as f:
    for line in f:
        line = line.split('  ')
        line[1] = line[1][1:-1]
        l1.append(int(line[0]))
        l2.append(int(line[1]))

k=0
for i in range(len(l1)):
    r=0
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            r+=1
    k+=l1[i]*r
print(k)
