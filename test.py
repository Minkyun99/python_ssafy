import sys
sys.stdin = open('input.txt')

N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

count_arr = [0] * (N+1)
result = 0


for i in range(M):
    count_arr[student[i]] += 1
    if count_arr[student[i]] >= K:
        result = student[i]
    if result > 0:
        break

print(result)