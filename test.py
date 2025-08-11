# 돌 뒤집기

import sys
sys.stdin = open('input.txt')

T = int(input())

for time in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(arr)
    for _ in range(M):
        i, j = map(int, input().split())
        print(f'프린트  {i}, {j}')
        for y in range(1, j+1):
            a = (i-1)-y
            b = (i-1)+y

            if a < 0 or a >= N or b < 0 or b >= N:
                continue

            print(a, arr[a])
            print(b, arr[b])
            if arr[a] == 0 and arr[b] == 0:
                arr[a], arr[b] = 1, 1
                print(arr)
            elif arr[a] == 1 and arr[b] == 1:
                arr[a], arr[b] = 0, 0
                print(arr)
            elif arr[a] != arr[b]:
                continue


    print(f'#{time}', end=' ')
    for row in arr:
        print(row, end=' ')