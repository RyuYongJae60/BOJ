# 1929
def prime_num(m, n):
    
    for i in range(m, n+1):
        if i == 0 or i == 1:
            continue
        
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                break
            
        else:
            print(i)
    

m, n = map(int, input().split())
prime_num(m, n)
