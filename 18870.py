# 18870
N = int(input())
x = list(map(int,input().split()))
x_ = sorted(set(x))

dic = {x_[i]: i for i in range(len(x_))}

for i in x:
    print(dic[i], end=' ')
