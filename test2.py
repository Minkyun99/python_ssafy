import sys
sys.stdin = open('input.txt')


def find_way(arr, x, N):
    global M, visited, result
    
    if len(visited) == N and visited[0] == 0:
        result = [0] * N*2
        for i in range(1, len(result)-1, 2):
            result[i] = visited[i//2]
            result[i+1] = visited[i//2]
        print(result)
        total = 0
        for j in range(0, len(result), 2):
            total += arr[result[j]][result[j+1]]

        if total < M:
            M = total
        
        result = []
        
        return
    
    for i in range(N):
        if i not in visited :
            visited.append(i)
            find_way(arr, i, N)
            visited.pop()


    
T = int(input())

for time in range(1, T+1):
    result = []
    N = int(input())
    M = 100*N
    visited = []
    arr = [list(map(int, input().split())) for _ in range(N)]

    find_way(arr, 0, N)

    print(f'#{time} {M}')
    