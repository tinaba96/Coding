N = int(input())
p = list(map(int, input().split()))

cnt = 1
P = [0,0]

for i in range(len(p)):
    P.append(p[i])

v = 1
target = P[-1]

if target == 1:
    print(cnt)
    exit()

for i in range(N, 2, -1):
    cnt += 1
    if P[target] == 1:
        break
    else:
        target = P[target]

print(cnt)






