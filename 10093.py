# 10093
A, B = map(int, input().split())
if A != B:
    mx_Num = max(A, B)
    mn_Num = min(A, B) + 1

    print(mx_Num-mn_Num)
    for i in range(mn_Num, mx_Num):
        print(i, end=' ')

else:
    print(A-B)
