N, B = input().split()
N = ''.join(reversed(N))
B = int(B)
s = 0

for i in range(len(N)):
    a = ord(N[i])
    
    if 48 <= a <= 57:
        s += (a-48) * (B**i)

    else:
        s += (a-55) * (B**i)

print(s)
