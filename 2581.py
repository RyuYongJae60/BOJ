# 2581
M = int(input())
N = int(input())
l = []

for i in range(M, N+1):
    a = 0
    if i>1:
        for j in range(2, i):
            if i%j == 0:
                a = a+1
                break

        if a == 0:
            l.append(i)

if len(l) == 0:
    print(-1)

else:
    print(sum(l))
    print(l[0])
