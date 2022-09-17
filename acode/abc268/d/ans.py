from itertools import permutations

def solve(n, m, s, t, min_chars=3, max_chars=16):
    T = set(t)
    def satisfied(x):
        return (min_chars <= len(x) <= max_chars) and (not x in T)
    def dfs(v, i, num, x):
        if i == n:
            return [x]
        res = []
        for k in range(1, num+1):
            y = x + ("_" * k) + v[i]
            res += dfs(v, i+1, num-k, y)
        #print(res)
        return res
    num = max_chars - len("".join(s))
    for v in permutations(s): # since we use permutation, it is no need to use used[] like video editorial
        for x in dfs(v, 1, num, v[0]):
            if satisfied(x):
                return x
    return -1

n, m = map(int, input().split())
s = [input() for i in range(n)]
t = [input() for i in range(m)]
print(solve(n, m, s, t))
