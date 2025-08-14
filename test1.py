T = int(input())

for time in range(1, T+1):
    arr = list(input().split())
    N = len(arr)
    stack = [0] * 256
    top = -1
    print_txt = ''
    for token in arr:
        if token == '.':
            print_txt = stack[0]
            break
        elif token not in '(+-*/)':
            top += 1
            stack[top] = int(token)
        else:
            if top > 0:
                a = stack[top]
                top -= 1
                b = stack[top]
                top -= 1
                if token == '+':
                    top += 1
                    stack[top] = b+a
                elif token == '-':
                    top += 1
                    stack[top] = b-a
                elif token == '*':
                    top += 1
                    stack[top] = b*a
                elif token == '/':
                    top += 1
                    stack[top] = int(b/a)
            else:
                print_txt = 'error'
                break

    if top == 0:
        print(f'#{time} {print_txt}')
    else:
        print(f'#{time} error')

