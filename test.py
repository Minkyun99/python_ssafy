import sys
sys.stdin = open('input.txt')
import time as ti

starts = ti.time()


def stack_top(x, result):
    global the_result, top

    if x == len(arr):
        if result >= top:
            the_result = min(result, the_result)
        return the_result

    stack_top(x+1, result)
    stack_top(x+1, result + arr[x])

T = int(input())

for time in range(1, T+1):
    N, top = map(int, input().split())
    arr = list(map(int, input().split()))

    the_result = 200000
    result = 0

    stack_top(0, result)

    print(f'#{time} {the_result - top}')


ends = ti.time()

t = ends - starts

print(t)