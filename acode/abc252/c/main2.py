N = int(input())

rail = []
ans = [0 for i in range(10)]
mp = [0 for i in range(10)]
cnt = [0 for i in range(10)]

for i in range(N):
    S = str(input())
    rail.append(S)
 
for j in range(10):
    ch = set()
    ch.add(rail[0][j])
    for k in range(1, N):
        ch.add(rail[k][j])
    cnt[j] = N - len(ch) + 1

for i in range(N):
    for e in range(10):
        ans[int(rail[i][e])] = max(e, ans[int(rail[i][e])])

#print(ans)
for k in range(10):
    if cnt[k] > 1:
        ans[k] = 10*(cnt[k]-1)

print(min(ans))
#print(ans)

#print(min(ans) + 10*cnt[min(ans)]-10)


