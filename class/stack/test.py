# 1
# 3 3
# 0 1 0
# 0 1 0
# 0 1 0

T = int(input())

for time in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    max_value = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                start = arr[i][j]
                for x in range(4):
                    for y in range(1, N):
                        r = i + dr[x] * y
                        c = j + dc[x] * y

                        if r < 0 or r >= N or c < 0 or c >= N:
                            continue
                        
                        while arr[r][c] == 1:
                            start += arr[r][c]

                if start >= 2 and max_value < start:
                    max_value = start
    print(f'#{time} {max_value}')


                    