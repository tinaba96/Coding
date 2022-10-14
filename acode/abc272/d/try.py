# i think the algorithm is correct
# but recursion is too heavy in this case for python
# therefore we should use queue and while loop


import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)

#pypyjit.set_param('max_unroll_recursion=-1')


N, M = list(map(int, input().split()))

dp = [[-1 for i in range(N)] for j in range(N)]

dp[0][0] = 0

if M > 320000:
    for l in range(N):
        print(*dp[l])
    exit()

rang = set()

for i in range(600):
    for j in range(i, 600):
        if M == i**2 + j**2:
            #print(i, j)
            rang.add((i, j))
            rang.add((j, i))

rang = list(rang)
#print('range')
#print(rang)

d = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

def next(now):
    x, y = now
    #print(rang)
    for ne in rang:
        ab, an = ne
        for g in d:
            b = ab*g[0]
            n = an*g[1]
            if x+b >= N or y+n >= N:
                continue
            if x+b < 0 or y+n < 0:
                continue
            #print('ccc')
            #print(b, n)
            if dp[x+b][y+n] == -1:
                dp[x+b][y+n] = 10**8

            if dp[x+b][y+n] > dp[x][y]+1:
                dp[x+b][y+n] = dp[x][y]+1
                next((x+b, y+n))

next((0, 0))

for l in range(N):
    print(*dp[l])


