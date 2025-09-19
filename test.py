import sys
sys.stdin = open('input.txt')


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_value = 0
for i in range(n):
    for j in range(n):
        count = 0
        for idx in range(3):
            r = j + idx
            if r < 0 or r >= n:
                continue
            count += grid[i][r] 

        max_value = max(count, max_value)

print(max_value)

