# 1037
N = int(input())
A = list(map(int, input().split()))
A.sort()

if N == 1:
    print(A[0]**2)

else:
    print(A[0]*A[-1])
