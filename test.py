import sys
sys.stdin = open('input.txt')

T = int(input())

for time in range(1, T + 1):
    N, M = map(int,input().split())

    arr = [list(input()) for _ in range(N)]

    No_same = []
    color = ['W', 'R', 'B']
    count = [[0] * 3 for _ in range(N)]

    for i in range(N):
        result = [0] * 3
        for j in range(M-1):
            if arr[i][j] != arr[i][j+1]:
                No_same.append(i)
                break
            if arr[i][j] == 'W':
                result[0] += 1
            elif arr[i][j] == 'R':
                result[1] += 1
            else:
                result[2] += 1
        
        for x in range(3):
            count[i][x] = result[x]
        


    print(No_same)
    print(count)
