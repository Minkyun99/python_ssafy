import sys
sys.stdin = open('input.txt')

def min_price(x, result):
    global min_value
    if x == len(arr):
        if result < min_value:
            min_value = result
        return
     
    if result > min_value:
        return
     
 
    for i in range(len(arr)):
        if not visited_x[i]:
 
            visited_x[i] = 1       
            min_price(i,result + arr[x][i])
            visited_x[i] = 0
         
 
T = int(input())
for time in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_value = 15000
    result = 0
    visited_x = [0] * len(arr)
 
    min_price(0, result)
    print(f'#{time} {min_value}')