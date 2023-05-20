# 1269
A, B = map(int, input().split())
dic = {}

a = list(map(int, input().split()))
b = list(map(int, input().split()))


for i in a:
    dic[i] = 1

for i in b:
    if i in dic:
        dic[i] += 1

    else:
        dic[i] = 1

c = 0
for i in dic:
    if dic[i] == 1:
        c += 1

print(c)
