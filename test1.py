import random
import string

def generate_palindrome(length):
    half = ''.join(random.choices(string.ascii_uppercase, k=(length+1)//2))
    if length % 2 == 0:
        return half + half[::-1]
    else:
        return half + half[-2::-1]

def generate_case(N, M):
    # 전체 배열 초기화
    board = [[random.choice(string.ascii_uppercase) for _ in range(N)] for _ in range(N)]
    
    # 회문 위치 결정
    is_horizontal = random.choice([True, False])
    start_row = random.randint(0, N-1)
    start_col = random.randint(0, N-M)
    
    palindrome = generate_palindrome(M)
    
    if is_horizontal:
        for i in range(M):
            board[start_row][start_col + i] = palindrome[i]
    else:
        for i in range(M):
            board[start_row + i][start_col] = palindrome[i]
    
    # 문자열로 변환
    board_lines = [''.join(row) for row in board]
    return board_lines, palindrome

def generate_test_cases(test_cases):
    output = []
    output.append(str(len(test_cases)))
    for idx, (N, M) in enumerate(test_cases):
        output.append(f"{N} {M}")
        board_lines, palindrome = generate_case(N, M)
        output.extend(board_lines)
        # 회문도 확인용 출력 가능
        # print(f"Test case {idx+1} palindrome: {palindrome}")
    return '\n'.join(output)

# 예시: N=12,13,15, M 임의로 설정
test_cases = [(12,6), (13,7), (15,8)]
result = generate_test_cases(test_cases)

with open("test_cases.txt", "w") as f:
    f.write(result)

print(result)
