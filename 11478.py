# 11478
s = input()
q = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        a = s[i: j+1]
        q.add(a)

print(len(q))
