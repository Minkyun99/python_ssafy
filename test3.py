import sys
sys.stdin = open('input.txt')

T = int(input())

for time in range(1, T+1):
    arr = []
    N = int(input())
    print(N)
    arr += (input().split())
    print(arr)

    result = []
    if N % 2 == 0:
        for i in range(N//2):
            result.append(arr[i])
            result.append(arr[N//2 + i])
    else:
        for i in range(1, N//2):
            result.append(arr[i-1])
            result.append(arr[N//2+i])


    print(result)
