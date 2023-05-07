# 25305
n, k = map(int, input().split())
q = list(map(int, input().split()))
q.sort(reverse=True)
print(q[k-1])
