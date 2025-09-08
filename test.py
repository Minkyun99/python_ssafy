import sys
sys.stdin = open('input.txt')


T = int(input())

for time in range(1, T+1):
    N, M = map(int, input().split())

    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    container = sorted(container)
    truck = sorted(truck)

    count = 0
    
    if len(container) > len(truck):
        while truck:
            a = container.pop()
            b = truck.pop()
            if a <= b:
                count += a
            else:
                truck.append(b)
    elif len(container) == len(truck):
        for i in range(len(container)):
            if container[i] <= truck[i]:
                count += container[i]
    else:
        while container:
            a = container.pop()
            b = truck.pop()
            if a <= b:
                count += a
            else:
                truck.append(b)


    print(f'#{time} {count}')
            