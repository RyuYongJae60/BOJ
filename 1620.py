# 1620
N, M = map(int, input().split())

l = [input() for i in range(N)]

dic = {}
for i, j in enumerate(l):
    dic[str(i+1)] = j

dic2 = {}
for i, j in dic.items():
    dic2[j] = i


q=[]
for i in range(M):
    a = input()
    
    if (a in dic) == True:
        q.append(dic.get(a))
        
    else:
        q.append(dic2.get(a))


for i in q:
    print(i)
        
