# trie tree?

import sys
sys.setrecursionlimit(505050)

n = int(input())
s = [[input(), i] for i in range(n)]
ans = [-1 for i in range(n)]

def divide(c, l):
    global ans
    if len(l) == 1:
        # print(l, c)
        ans[l[0][1]] = c-1
    else:
        d = dict()
        for x in l:
            if len(x[0]) == c:
                ans[x[1]] = c
            else:
                nc = x[0][c]
                if nc in d:
                    d[nc].append(x)
                else:
                    d[nc] = [x]
        for nk in d:
            divide(c+1, d[nk])
divide(0, s)
for x in ans:
    print(x)


