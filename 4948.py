# 4948
def Bertran(n):
    l = [True] * (2*n+1)
    c = 0

    for i in range(2, int((2*n)**0.5) + 1):
        if l[i] == True:
            for j in range(i*2, (2*n)+1, i):
                l[j] = False
        

    for i in range(n+1, 2*n+1):
        if l[i] == True:
            c += 1


    return c


q = []
while True:
    n = int(input())

    if n == 0:
        for i in q:
            print(i)
        break

    else:
        q.append(Bertran(n))


