import sys
sys.stdin = open('input.txt')

def break_wall(arr, N, W, H, x, y, result):
    global max_value
    if N == 0:
        if max_value < result:
            max_value = result
        return 
    
    if x < 0 or x >= H or y < 0 or y >= W:
        return


    for i in range(H):
        for j in range(W):
            dr = [1, -1, 0, 0]
            dc = [0, 0, 1, -1]

            count = 1
            q_arr = []
            q_arr.append([i, j, arr[i][j]-1])

            visited = [[0] * W for _ in range(H)]
            visited[i][j] = 1

            while q_arr:
                a = q_arr.pop(0)

                for z in range(a[2]):
                    for idx in range(4):

                        x = a[0] + dr[idx] * z
                        y = a[1] + dc[idx] * z

                        if x < 0 or x >= H or y < 0 or y >= W or arr[x][y] == 0:
                            continue

                        if visited[x][y] == 0:

                            if arr[x][y] > 1:
                                count += 1
                                q_arr.append([x, y, arr[x][y]-1])
                                visited[x][y] = visited[i][j] + 1
                            elif arr[x][y] == 1:
                                count += 1
                                visited[x][y] = visited[i][j] + 1

            break_wall(arr, N-1, W, H, i, j, result+count)





T = int(input())

for time in range(1, T+1):
    N, W, H = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(H)]



    result = 0
    max_value = 0
    break_wall(arr, N, W, H, 0, 0, result)
    print(max_value)









                # if 1 >= arr[j][i] > 0:
                #     count += arr[j][i]
                # elif arr[j][i] > 1:
                #     n = arr[j][i]
                #     for idx in range(n):
                #         x = i + idx*n
                #         y = j + idx*n

                #         if x < 0 or x >= N or y < 0 or y >= N or arr[x][y] > 1:
                #             continue

                #         count += arr[x][y]

                #         if arr[x][y] > 1:
                #             break_wall(arr, )