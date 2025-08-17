import sys
sys.stdin = open('input.txt')

T = int(input())

for time in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    isTwice = False

    for i in range(9):
        total = []
        c_total = []
        for j in range(9):
            if arr[i][j] not in total and arr[j][i] not in c_total: 
                total.append(arr[i][j])
                c_total.append(arr[j][i])
            else:
                print(arr[i][j], i, j, '중복')
                isTwice = True
                total = []
                c_total = []
                break
            for m in range(0, 9, 3):
                for n in range(0, 9, 3):
                    total_square = []
                    for c in range(3):
                        for r in range(3):
                            a = m + c
                            b = n + r
                            if a < 0 or a >= 9 or b < 0 or b >= 9:
                                break
                            if arr[a][b] not in total_square:
                                total_square.append(arr[a][b])
                            else:
                                isTwice = True
                                total_square = []
                                break    
            if isTwice == True:
                break
    if isTwice == True:
        print(f'#{time} 0')
    else:
        print(f'#{time} 1')