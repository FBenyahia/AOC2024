l1 = []
l2 = []

with open("inputs/day1.txt", 'r') as f:
    for line in f:
        print(line)
        line = line.split('  ')
        line[1] = line[1][1:-1]
        l1.append(int(line[0]))
        l2.append(int(line[1]))
k = 0
l1Sorted = l1 + []
l2Sorted = l2 + []
l1Sorted.sort()
l2Sorted.sort()
for i in range(len(l1Sorted)):
    k+= abs(l1Sorted[i] - l2Sorted[i])

print(k)


#Part 2
k=0
for i in range(len(l1)):
    r=0
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            r+=1
    k+=l1[i]*r
print(k)
