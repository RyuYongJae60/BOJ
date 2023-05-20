# 1269
A, B = map(int, input().split())

a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

a_ = a-b
b_ = b-a

q = len(a_) + len(b_)
print(q)
