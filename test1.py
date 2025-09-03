import sys
sys.stdin = open('input.txt')

T = int(input())

for time in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]
    pwd_result = []
    pwd = ''
    if M <= 26:
        for i in range(N):
            for j in range(M):
                q = 0
                while arr[i][j+q] != '0':
                    pwd += arr[i][j+q]
                    q += 1
                    break
                pwd_result.append(pwd)

    print(pwd_result)

    hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    
    result = ''
    for i in range(len(pwd)):
        result += hex_dict[pwd[i]]

    result_2 = ''
    r = 0
    for j in range(len(result)-1, -1, -1):
        if result[j] == '1':
            result_2 = result[j-55:j+1]
            break

    ratio_result = []
    str_str = ''

    for x in range(0,len(result_2), 7):
        for i in range(7):
            str_str += result_2[x+i]
        ratio_result.append([str_str])
        str_str = ''

    ratio = {0: [3,2,1,1], 1:[2,2,2,1], 2:[2,1,2,2], 
             3:[1,4,1,1], 4:[1,1,3,2], 5:[1,2,3,1], 
             6:[1,1,1,4], 7:[1,3,1,2], 8:[1,2,1,3], 
             9:[3,1,1,2]}
    


    all_ratios = []
    for item in ratio_result:

        pattern = item[0]
        
        ratios = []
        current_char = pattern[-1]
        count = 1
        
        for i in range(len(pattern) - 2, -1, -1):
            if pattern[i] == current_char:
                count += 1
            else:
                ratios.append(count)
                count = 1
                current_char = pattern[i]
        ratios.append(count)
        all_ratios.append(ratios[::-1])

    result_result = []
    for i in range(len(all_ratios)):
        for key, value in ratio.items():
            if all_ratios[i] == value:
                result_result.append(key)

    p = 0
    p_odd = 0
    for i in range(len(result_result)):
        if i % 2 == 0:
            p += result_result[i]
        else:
            p_odd += result_result[i]

    if (p*3)+p_odd % 10 == 0:
        print(sum(result_result))




            

            

            





    