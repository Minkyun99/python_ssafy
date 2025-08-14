import sys
sys.stdin = open('input.txt')

for time in range(1, 11):
    N = int(input())
    arr = list(input())
    postfix = []

    stack = [''] * N
    top = -1

    for token in arr:
        if token in '+':
            top += 1
            stack[top] = token
        else:
            postfix += str(token)

    item = 0
    for i in postfix:
        item += int(i)

    print(f'#{time} {item}')