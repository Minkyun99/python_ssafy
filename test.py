import sys
sys.stdin = open('input.txt')

N = int(input())
student = int(input())

arr = list(map(int, input().split()))


candidate = []
count = [0] * (student+1)

for i in range(len(arr)):
    if len(candidate) < N :
        runner = arr.pop(0)
        candidate.append(runner)
        count[runner] += 1

    else :
        runner = arr.pop(0)
        count[runner] += 1

        if runner not in candidate:
            total = 0
            old = []
            for j in range(len(candidate)):
                if count[candidate[j]] > count[runner]:
                    continue
                elif count[candidate[j]] <= count[runner]:
                    total += 1
                    old.append(j)
            print(old)
            if total > 1 : 
                min_value = count[old[0]]
                b = 0
                for i in range(1, len(old)):
                    if min_value > count[old[i]]:
                        min_value = count[old[i]]
                        b = old[i]
                candidate.pop(old[i])
                candidate.append(runner)
                
            elif total == 1:
                count[old[0]] = 0
                candidate.pop(old[0])
                candidate.append(runner)
            



a = sorted(candidate)
for x in range(len(a)):
    print(a[x], end=' ')
