# 25191
n = int(input())
a, b = map(int,input().split())

r = 0
r += a//2
r += b

if r > n:
    print(n)

else:
    print(r)
