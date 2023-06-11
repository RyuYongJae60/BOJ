# 9610
dic = {'Q1':0, 'Q2':0, 'Q3':0, 'Q4':0, 'AXIS':0}

n = int(input())
for i in range(n):
    x, y = map(int, input().split())

    if x==0 or y==0:
        dic['AXIS'] += 1

    elif x >= 1:
        if y >= 1:
            dic['Q1'] += 1
        
        else:
            dic['Q4'] += 1
    else:
        if y >= 1:
            dic['Q2'] += 1
        
        else:
            dic['Q3'] += 1


for i in dic:
    print(i+':', dic[i])
