import sys
sys.stdin = open('input3.txt')

ladder_arr = [list(map(int, input().split())) for _ in range(100)]

print(ladder_arr)