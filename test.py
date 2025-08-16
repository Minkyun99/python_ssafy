import sys
sys.stdin = open('input.txt')

T = int(input())

for time in range(1, T+1):
    found = False
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]

    # 가로 회문
    for i in range(N):
        for j in range(N-M+1):
            str = ''
            for x in range(M//2):
                a = j + x
                b = j + (M-1) - x
                if arr[i][a] == arr[i][b]:
                    str += arr[i][a]
                else:
                    str = ''
                    break
            if len(str) == M//2:
                print(f'#{time}', end=' ')
                # 앞부분
                for y in range(len(str)):
                    print(str[y], end='')
                # 가운데 글자 (홀수일 경우)
                if M % 2 == 1:
                    print(arr[i][j + M//2], end='')
                # 뒷부분
                for z in range(len(str)-1, -1, -1):
                    print(str[z], end='') 
                print()
                found = True
                break
        if found:
            break

    # 세로 회문
    if not found:
        for u in range(N):
            for k in range(N-M+1):
                str = ''
                for x in range(M//2):
                    a = k + (M-1) - x
                    b = k + x
                    if arr[b][u] == arr[a][u]:
                        str += arr[b][u]
                    else:
                        str = ''
                        break
                if len(str) == M//2:
                    print(f'#{time}', end=' ')
                    # 앞부분
                    for y in range(len(str)):
                        print(str[y], end='')
                    # 가운데 글자 (홀수일 경우)
                    if M % 2 == 1:
                        print(arr[k + M//2][u], end='')
                    # 뒷부분
                    for z in range(len(str)-1, -1, -1):
                        print(str[z], end='') 
                    print()
                    found = True
                    break
            if found:
                break
