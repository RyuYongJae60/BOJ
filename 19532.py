# 19532
a = list(map(int, input().split()))

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a[0]*i + a[1]*j == a[2] and a[3]*i + a[4]*j == a[5]:
            print(i, j)

