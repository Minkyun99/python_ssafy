import sys
sys.stdin = open('input.txt')


T = int(input())

for time in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    def find_cart(x, result):
        global min_value
        
        # 가지치기: 현재 결과가 이미 최솟값보다 크면 중단
        if result >= min_value:
            return
        
        if x == N:
            if min_value > result:
                min_value = result
            return
                    
        for i in range(N):
            if arr[x][i] == 0:  # 연결되지 않은 경우
                continue
            
            if not visited[i]:  # 아직 방문하지 않은 경우
                visited[i] = 1
                find_cart(x+1, result + arr[x][i])
                visited[i] = 0
    result = 0
    visited = [0] * N
    min_value = 100000
    find_cart(0, result)
    print(min_value)


