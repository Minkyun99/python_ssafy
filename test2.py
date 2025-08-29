import sys
sys.stdin = open('input.txt')

N = int(input())
p = [0] * (N+1)
left = [0] * (N+1)
right = [0] * (N+1)
arr = []
for i in range(1, N+1):
    arr += [list(input().split())]

cal = {'+':1, '-': 1, '*':2, '/':2}

for j in range(N):
    if arr[j][1] not in cal:
        if j % 2 == 0:
            left[j+1] = int(arr[j][1])
        else:
            right[j+1] = int(arr[j][1])
    else:
        if int(arr[j][0]) % 2 == 0:
            left[int(arr[j][0])] = arr[j][1]
        else:
            right[int(arr[j][0])] = arr[j][1]


def pre_order(v):
    if v == 0:
        return
    
    pre_order(left(v))

    pre_order(right(v))
    
    if pre_order(v) == '-':
        return left(v*2) - right(v*2+1)
    else:
        return left(v*2) * right(v*2+1)
    
result = pre_order(0)