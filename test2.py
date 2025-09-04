import sys
sys.stdin = open('input.txt')


def find_way(arr, x, y, result,visited, N):
    global M
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    
    if len(result) == N:
        total = sum(result)
        if total < M:
            M = total
        result = []
        return
    
    for i in range(N):
        if i not in visited:
            result.append(arr[x][i])
            visited.append(i)
            find_way(arr, x + 1, i, result, visited, N)
            visited.pop()


    
T = int(input())

for time in range(1, T+1):

    N = int(input())
    M = 100*N
    arr = [list(map(int, input().split())) for _ in range(N)]

    a = find_way(arr, 0, 0, [], [], N)

    print(f'#{time} {M}')
    