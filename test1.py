import sys
sys.stdin = open('input.txt')

x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())


rec_arr = [[0]*2000 for _ in range(2000)]



for idx in range(3):
    for i in range(x1[idx]+1000, x2[idx]+1000):
        for j in range(y1[idx]+1000, y2[idx]+1000):
            rec_arr[i][j] += 1



M = (x2[2] - x1[2]) * (y2[2] - y1[2])


count = 0
minus_count = 0
for i in range(2000):
    for j in range(2000):
        if rec_arr[i][j] == 1:
            count += 1
        elif rec_arr[i][j] == 2:
            minus_count += 1



print(count - (M - minus_count))




