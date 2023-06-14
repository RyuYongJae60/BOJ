# 10162
T = int(input())

a = 300
b = 60
c = 10

t1 = T//a
T = T%a

t2 = T//b
T = T%b

t3 = T//c
T = T%c


if T == 0:
    print(t1, t2, t3)

else:
    print(-1)
