# 1297
D, H, W = map(int, input().split())
x = (D**2 / (H**2 + W**2))**0.5 * W
y = (D**2 / (H**2 + W**2))**0.5 * H

print(int(y), int(x))
