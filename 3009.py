# 3009
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x = [x1, x2, x3]
y = [y1, y2, y3]

x4 = 0
y4 = 0

for i in set(x):
    if x.count(i) == 1:
        x4 = i

for i in set(y):
    if y.count(i) == 1:
        y4 = i

print(x4, y4)
