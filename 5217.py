# 5217
t = int(input())
num = []
pair = []

for i in range(t):
    n = int(input())
    num.append(n)

    sum = []
    for j in range(1, n):
        for k in range(j+1, n):
            if j+k == n:
                sum.append([j, k])

    pair.append(sum)

for i in range(len(num)):
    print('Pairs for ' + str(num[i]) + ':', end=' ')

    c = 0
    for j in pair[i]:
        if c >= 1:
            print(', ', end='')

        print(str(j[0]), str(j[1]), end='')
        c += 1

    print()        
