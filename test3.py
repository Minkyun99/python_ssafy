
def search(arr, idx, result):
    if idx == len(arr):
        if len(result) == 2:
            return [result]
        else:
            return []
    
    a = search(arr, idx+1, result)
    b = search(arr, idx+1, result + [arr[idx]])

    return a + b
    




arr = [1,2,3]
result = []
c = search(arr, 0, result)

def permute(arr, result):
    # 재귀 종료 조건: 결과 리스트의 길이가 2가 되면 출력
    if len(result) == 2:

        return [result]

    # 재귀 호출
    for i in range(len(arr)):
        # 현재 요소를 포함하지 않는 경우
        # 이 코드의 핵심은 'arr'를 재귀 호출 시마다 변경하여 중복을 피하는 것입니다.
        if arr[i] not in result:
            permute(arr, result + [arr[i]])

# 함수 호출
arr = [1, 2, 3]
permute(arr, [])

print(c)


# def Main(x):
#     KFC(x)
#     return 

def KFC(x):
    if x == 3:
        return
    print(x, end=' ')
    KFC(x+1)
    KFC(x+1)
    print(x, end=' ')

KFC(0)
