
N = int(input())
arr = [list(input()) for _ in range(8)]

t_count = 0

for i in range(8):
    count = 0
    for j in range(8):
        for idx in range(1, N//2):
            if i-idx < 0 or i-idx >= 8 or j+idx < 0 or j+idx >= 8:
                if arr[i-idx][j-idx] != arr[i+idx][j+idx]:
                    break
                count += 1
        if count > 0:
            t_count += count

    print(t_count)
