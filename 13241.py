# 13241
# lcm(a, b) = |ab|/gcd(a,b)

def gcd(a, b):
    while (b != 0):
        r = a%b
        a = b
        b = r

    return a


A, B = map(int, input().split())
print(abs(A*B)//gcd(A, B))
