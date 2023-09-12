# コピーによる、完全な参照渡し（オブジェクトへの参照私ではなく。）


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


N, M = list(map(int, input().split()))
mp = [[] for j in range(N+1)]

for i in range(M):
    A, B, C = list(map(int, input().split()))
    mp[A].append((B, C))
    mp[B].append((A, C))
    

#print(mp)

ans = 0

def solve(base, tmp, seen):
    global ans
    seen[base-1] = True
    ans = max(ans, tmp)
    cnt = 0
    for b, c in mp[base]:
        cnt += 1
        #print('base: ', base, 'cnt: ', cnt)
        #print(b,c)
        if seen[b-1] == True:
            continue
        #tmp = max(solve(b, tmp, seen), tmp)
        seenCp = seen[:]
        solve(b, tmp+c, seenCp)
        #seen[b-1] = False
    return max(ans, tmp)
        
#print(mp)

final = 0
for i in range(N):
    base = i+1
    seen = [False]*N
    #print(seen)
    tmp = 0
    seen[i] = True
    final = max(final, solve(base, tmp, seen))
    #print('i: ', i+1, 'final: ', final)
    #print('------')

#print(final)
print(ans)

# similar to video editorial

