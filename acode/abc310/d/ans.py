# same as video editorial

N, T, M = map(int, input().split())
relations = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    relations[b].append(a)

ans = 0
def dfs(state, p, t):
    global ans
    if p == N:
        if max(state) == T-1:
            ans += 1
        return
    nxt = set([i for i in range(min(t+1, T))])
    for other in relations[p]:
        if state[other] in nxt:
            nxt.remove(state[other])
    for ti in nxt:  # ti is team index
        state[p] = ti # p belongs to team ti
        if ti == t: # t is the new empty team
            dfs(state, p+1, min(t+1, T-1))
            #dfs(state.copy(), p+1, min(t+1, T-1))
        else:
            dfs(state, p+1, t)
            #dfs(state.copy(), p+1, t)
        state[p] = None

dfs([None]*N, 0, 0)
print(ans)
