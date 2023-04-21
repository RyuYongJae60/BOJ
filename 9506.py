# 9506
l = []

while True:
    a = []
    n = int(input())
    if n == -1:
        break

    else:
        for i in range(1, n):
            if n % i == 0:
                a.append(i)

        if n == sum(a):
            q = ''
            for i in a:
                if i == max(a):
                    q += str(i)
    
                else:
                    q += str(i) + ' + '
            
            l.append(str(n) + ' = ' + q)

        else:
            q = str(n) + ' is NOT perfect.'
            l.append(q)

for i in l:
    print(i)
