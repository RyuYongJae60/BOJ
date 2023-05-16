# 7785
import sys
n = int(sys.stdin.readline())
l = {}

for i in range(n):
    name, state = map(str, sys.stdin.readline().split())
    l[name] = state
    
q = []

for i in l.keys():
    if l.get(i) == 'enter':
        q.append(i)


for i in sorted(q, reverse = True):
    print(i)
