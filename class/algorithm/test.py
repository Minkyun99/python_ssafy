import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for _ in range(T):
    time, N = map(input().split())
    str = input().split()

    counting_sort = [0]*10
    result = [0] * N

    dic_str = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}

    for i in str:
        counting_sort[dic_str[i]] += 1

    for j in range(len(counting_sort)):
        dic_str[j]



    print(f'#{time}')
    i = 0
    for key in dic_str.keys():
        print(counting_sort[i] * f'{key} ', end='') 
        i += 1
