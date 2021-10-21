from collections import defaultdict

ma = defaultdict(list)

N = int(input())
#ma = [[] for j in range(10**9)]
#p = {}
for i in range(N):
    x, y = list(map(int, input().split()))
    ma[x].append(y)
    #p[x] = y
cnt = 0
ans = []
print(ma)
for i in range(len(ma)):
    for j in range(len(ma[i])):
        for k in range(i+1, len(ma)):
            if ma[i][j] in ma[k]:
                ans.append((i,k))
                #print(i,k)

for i in range(len(ans)):
    ele = ans.pop()
    if ele in ans:
        cnt += 1
print(cnt)


