# 25192
q = set()
t = 0

n = int(input())
for i in range(1, n+1):
    a = input()
    if a == 'ENTER':
        t += len(q)
        q = set()
        pass

    else:
        q.add(a)

t += len(q)

print(t)
