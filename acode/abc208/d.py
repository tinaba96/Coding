N, M = list(map(int, input().split()))
m = [[0] for j in range(N)]

for k in range(M):
    a, b, c = list(map(int, input().split()))
    m[a] = (b, c)

ans = 0
def f(s, t, k):
    arr = []
    for e in range(len(m[s])):
        tmp = m[s][e][0] 
        if tmp not in arr:
            arr.append(tmp)
        else:
            break
        if(tmp == t):
            break
        score += m[s][e][1]
        score += f(tmp, t, k)
    ans_score = min(ans_score, score)
    return ans_score



for s in range(N):
    for t in range(N):
        for k in range(N):
            ans += f(s, t, k)

print(ans)


