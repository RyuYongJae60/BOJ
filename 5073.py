# 5073
l = []
while True:
    a = list(map(int, input().split()))
    if a[0] == a[1] == a[2] == 0:
        for i in l:
            print(i)

        break

    if a[0] == a[1] == a[2]:
        l.append('Equilateral')

    else:
        m = max(a)
        q = set(a)
        a.remove(m)
        s = sum(a)

        if m >= s:
            l.append('Invalid')

        else:
            if len(q) == 2:
                l.append('Isosceles')

            else:
                l.append('Scalene')
