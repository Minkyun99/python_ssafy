import sys
sys.stdin = open('input.txt')

T = int(input())

for time in range(1, T+1):
    N = int(input())
    arr = [0]
    arr += list(map(int, input().split()))

    bulb = [0]* (N+1)

    count = 0
    for i in range(1, N+1):
        if arr[i] != bulb[i]:
            count += 1
            for j in range(i, N+1, i):
                if bulb[j] == 1:
                    bulb[j] = 0
                else:
                    bulb[j] = 1
    print(f'#{time} {count}')

                
                


