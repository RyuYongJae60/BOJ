# 9713
N = int(input())

num = []

for i in range(N):
    num.append(int(input()))
    

for i in num:
    sum = 0
    for j in range(1, i+1):
        if j % 2 == 1:
            sum += j
            
    print(sum)
