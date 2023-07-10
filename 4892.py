# 4892
l = []

while True:
    n0 = int(input())
    if n0 == 0:
        break

    n1 = 3*n0
    if n1%2 == 0:
        n2 = n1/2
    
    else:
        n2 = (n1+1)/2

    n3 = 3*n2
    n4 = int(n3//9)

    if n1%2==0:
        l.append(['even', n4])
    
    else:
        l.append(['odd', n4])

    
for i, enum in enumerate(l):
    print(str(i+1)+'.', enum[0], enum[1])
