# 11557
T = int(input())
l = []

for _ in range(T):
    N = int(input())
    dic = {}

    for _ in range(N):
        a, b = input().split()

        dic[a] = int(b)

    for k, v in dic.items():
        if v == max(dic.values()):
            l.append(k)

for i in l:
    print(i)
