# 14215
l = list(map(int, input().split()))
l.sort()

# 삼각형 넓이 조건 : l[0] + l[1] > l[2]

if l[0] + l[1] > l[2]:
    print(sum(l))

else:
    print(l[0] + l[1] + (l[0]+l[1])-1)
