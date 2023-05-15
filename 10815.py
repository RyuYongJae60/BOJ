# 10815  # 이분탐색
def BS(array, target, start, end):
    if start > end:
        return 0

    mid = (start + end)//2

    if array[mid] == target:
        return 1

    elif array[mid] < target:
        return BS(array, target, mid+1, end)

    else:
        return BS(array, target, start, mid-1)


N = int(input())
a = list(map(int, input().split()))
a.sort()

M = int(input())
b = list(map(int, input().split()))

for i in b:
    print(BS(a, i, 0, N-1), end=' ')
