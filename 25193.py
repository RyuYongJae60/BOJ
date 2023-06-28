# 25193
N = int(input())
S = list(input())

c = S.count('C')

print(N//((N-c)+1))
