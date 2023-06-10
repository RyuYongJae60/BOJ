# 5063
N = int(input())
l = []

for i in range(N):
    r, e, c = map(int, input().split())
    s = e-c

    if r == s:
        l.append('does not matter')

    if r > s:
        l.append('do not advertise')

    if r < s:
        l.append('advertise')

for i in l:
    print(i)
