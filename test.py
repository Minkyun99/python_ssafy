import sys
sys.stdin = open('input.txt')

T = int(input())

for time in range(1, T + 1):
    N, A, B = map(int, input().split())

    arr = list(map(int, input().split()))
    arr = sorted(arr)
    arr = arr[::-1]

    A_arr = [0] * N
    B_arr = [0] * N
    for i in range(N):
        if N % 2 == 0:
            if A > B:
                for j in range(0, A, 2):
                    A_arr[j] = 1
            if A == B:
                for j in range(0, N, 2):
                    A_arr[j] = 1
            else:
                for j in range(0, B, 2):
                    B_arr[j] = 1
        else:
            if A > B:
                for j in range(0, N, 2):
                    A_arr[j] = 1
            else:
                for j in range(0, N, 2):
                    B_arr[j] = 1
    result = 0
    v_A =  1
    v_B =  1

    if A >= B:
        for i in range(N):
            if A_arr[i] == 1:
                A_arr[i] = arr[i] * v_A
                v_A += 1
            else:
                B_arr[i] = arr[i] * v_B
                v_B += 1
        result = sum(A_arr) + sum(B_arr)
    else:
        for i in range(N):
            if B_arr[i] == 1:
                B_arr[i] = arr[i] * v_B
                v_B += 1
            else:
                A_arr[i] = arr[i] * v_A
                v_A += 1
        result = sum(A_arr) + sum(B_arr)

    print(f'#{time} {result}')