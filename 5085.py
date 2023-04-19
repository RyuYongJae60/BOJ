# 5086
l = []

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    else:
        if b%a == 0:
            l.append('factor')
        
        elif a%b == 0:
            l.append('multiple')

        else:
            l.append('neither')

for i in l:
    print(i)
