import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict
#d = defaultdict(int)

ans = 0
N, M = list(map(int, input().split()))

mp = [[0 for i in range(N+1)] for j in range(N+1)]
smp = []

for m in range(M):
    C = int(input())
    a = list(map(int, input().split()))
    tmp = 0
    for c in a:
        tmp += 2**(c-1)
        #mp[m][a[c]-1] = 1
    smp.append(tmp)

ans = 0

model = 2**M-1
status = 0


cor = set()

def dfs(status, seen):
    global ans
    #print(status, ' : ', model)
    if status == model:
        cor.add(str(list(seen)))
        #print(bin(status))
        #print('sa')
        ans += 1

    if len(seen) == M:
        return
    for h in range(M):
        if h not in seen:
            seen.add(h)
            tmp_status = status
            status |= smp[h]
            dfs(status, seen)
            seen.remove(h)
            status = tmp_status
        #else:
            #print('as')


#print(mp)
for p in range(M):
    seen = set()
    #jprint(bin(smp[p]))
    if smp[p] & (1 << 0):
        #print('yrs')
        status |= smp[p]
        seen.add(p)
        #print(bin(status))
        dfs(status, seen)


print(ans)
print(len(cor))
# why different
