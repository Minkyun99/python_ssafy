import sys
sys.stdin = open('input.txt')

T = int(input())

for time in range(1, T + 1):
    N, M = map(int, input().split())

    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    container.sort(reverse=True)
    truck.sort(reverse=True)

    total_weight = 0
    container_idx = 0
    truck_idx = 0
    
    while container_idx < len(container) and truck_idx < len(truck):
        if truck[truck_idx] >= container[container_idx]:
            total_weight += container[container_idx]
            truck_idx += 1
            container_idx += 1
        else:
            container_idx += 1

    print(f'#{time} {total_weight}')