T = int(input())


for time in range(1, T+1):

    N = int(input())
    arr = list(map(int, input()))

    count = 0
    max_value = 0
    for i in range(N):
        if arr[i] == 1:
            count += 1
            if max_value < count:
                max_value = count
        else:
            if max_value < count:
                max_value = count
            count = 0

    print(f'#{time} {max_value}')