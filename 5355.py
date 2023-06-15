# 5355
T = int(input())
t = []

for _ in range(T):
    l = input().split()
    
    r = float(l[0])

    for i in range(1, len(l)):
        a = l[i]
        
        if a == '@':
            r *= 3

        if a == '%':
            r += 5

        if a == '#':
            r -= 7

    t.append(r)


for i in t:
    print('{:.2f}'.format(i))
