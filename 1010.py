# 1010
def factor(a):
    if a <= 1:
        return 1

    return a*factor(a-1)



n = int(input())
for i in range(n):
    a, b = map(int, input().split())

    
    print((factor(b)//factor(b-a))//factor(a))
    
