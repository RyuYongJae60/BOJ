N = int(input())
cross_count = 1     # 대각선 칸의 개수. 분자+분모가 짝수 or 대각선 칸 홀수: ↗︎ . 반대는 ↙︎ 방향으로 진행.
prev_count_sum = 0  # 직전 대각선 까지의 누적 합

while True:
    if N <= prev_count_sum + cross_count:
        if cross_count % 2 == 1:        # 대각선 개수 홀수(↗︎)
            print(str((cross_count - (N - prev_count_sum - 1))) + '/' + str((N - prev_count_sum)))
            break


        else:
            print(str((N - prev_count_sum)) + "/" + str((cross_count - (N - prev_count_sum - 1))))
            break



    else:
        prev_count_sum += cross_count
        cross_count += 1 
