# 10214

T = int(input())

for _ in range(T):
    Y = 0
    K = 0

    for i in range(9):
        y, k = map(int, input().split())
        Y += y
        K += k

    if Y > K:
        print('Yonsei')

    elif Y < K:
        print('Korea')

    else:
        print('Draw')