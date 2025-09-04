import sys
sys.stdin = open('input.txt')

def find_way(arr, x, y, result, N, all_path):
    result.append(arr[x][y])
 
    if x == N-1 and y == N-1:
        all_path.append(sum(result))
      
    dr = [0, 1]
    dc = [1, 0]
 
    for i in range(2):
        r = x + dr[i]
        c = y + dc[i]
         
        if 0 <= r < N and 0 <= c < N:
            find_way(arr, r, c, result, N, all_path)
     
    result.pop()
T = int(input())
 
for time in range(1, T+1):
 
 
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    all_path = []
    find_way(arr, 0, 0, [], N, all_path)
    a = min(all_path)
 
    print(f'#{time} {a}')