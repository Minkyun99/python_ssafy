import sys
sys.stdin = open('input.txt')

# 함수 1 : 최대값 구하기 
def find_max_value(random_array):
    max_value = random_array[0]
    for i in range(len(random_array)):
        if max_value < random_array[i]:
            max_value = random_array[i]
    return max_value

# 함수 2 : 최소값 구하기
def find_min_value(random_array):
    min_value = random_array[0]
    for i in range(len(random_array)):
        if min_value > random_array[i]:
            min_value = random_array[i]
    return min_value


# 테스트 케이스 입력 받기
T = int(input())

# 테스트 케이스만큼 수행
for time in range(1, T+1):
    # 정수의 개수 = 배열의 길이 받기
    N = int(input())
    # 배열의 값 받기
    arr = list(map(int, input().split()))

    # 정렬된 값을 받을 새로운 배열 할당
    new_arr = []

    # 함수를 수행하되, 배열의 길이의 절반만 수행하기
    # 최대값과 최소값을 함께 정렬하기 때문에 배열의 길이에서 절반만 수행해야 함
    for i in range(5):
        # 최대값, 최소값 함수 수행
        max_value = find_max_value(arr)
        min_value = find_min_value(arr)

        # 최대값 먼저 append한 이후에 최소값 append 함
        new_arr.append(max_value)
        new_arr.append(min_value)

        # 정렬된 값은 기존 배열에서 삭제함
        arr.remove(max_value)
        arr.remove(min_value)
        
    print(f'#{time}', end=' ')
    for i in new_arr:
        print(i, end=' ')
    print()