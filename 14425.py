#14425
N, M = map(int, input().split())
s = {input() for i in range(N)}

l = [input() for i in range(M)]

c = 0

for i in l:
    if i in s:
        c += 1
        
print(c)
