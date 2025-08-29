import sys
sys.stdin = open('input.txt')

K = int(input())
arr = []

for i in range(6):
    arr += [list(map(int,input().split()))]

t = []

x = 0
y = 0

for j in range(6) :
    if arr[j][0] == 4:
        y = y + arr[j][1]
        t.append([x, y])
    elif arr[j][0] == 3:
        y = y - arr[j][1]
        t.append([x, y])
    elif arr[j][0] == 2:
        x = x - arr[j][1]
        t.append([x, y])
    else:
        x= x + arr[j][1]
        t.append([x, y])

print(t)


for i in range(3): 