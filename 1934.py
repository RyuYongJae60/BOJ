# 1934
T = int(input())
l = []

for i in range(T):
    a, b = map(int, input().split())
    num = []

    for i in range(1, a+1):
        if a%i == 0:
            if (i*b)%a == 0:
                num.append(i*b)

    l.append(min(num))

for i in l:
    print(i)
