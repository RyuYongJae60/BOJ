# 1764
N, M = map(int, input().split())
a = {}
l = []

for i in range(N):
    a[input()] = 1


for i in range(M):
    q = input()
    
    if (q in a) == True:
        a[q] += 1


for i in a:
    if a[i] == 2:
        l.append(i)


l.sort()
print(len(l))
for i in l:
    print(i)
