import sys
sys.stdin = open('input2.txt')

# 북 페이지 찾는 함수 작성
def search_book_page(total_page, find_page):
    # 이진탐색을 위한 start, end 변수 할당
    # start를 1로 주어야 함 (주어진 조건)
    start_page = 1
    end_page = total_page

    # 이진탐색 횟수를 세는 count 변수 할당
    count = 0

    # 이진탐색 시작
    while start_page <= end_page:
        # end_page가 홀수로 끝날 수도 있으니, 해당 값까지 반영해야 함
        half = int((start_page + end_page) / 2)
        if half == find_page:
            return count
            break
        elif half > find_page:
            end_page = half 
            count += 1
        elif half < find_page:
            start_page = half 
            count += 1
    return count

T = int(input())

for time in range(1, T+1):
    P, A, B = map(int,input().split())

    result_A = search_book_page(P, A)
    result_B = search_book_page(P, B)

    # return count 변수가 작은 사람을 출력함
    if result_A > result_B:
        print(f'#{time} B')
    elif result_A == result_B:
        print(f'#{time} 0')
    elif result_A < result_B:
        print(f'#{time} A')

