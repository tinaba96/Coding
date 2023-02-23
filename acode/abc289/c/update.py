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

model = 2**N-1
status = 0


cor = set()

def dfs(status, seen):
    global ans
    #print(seen)
    #print(bin(status), ' : ', bin(model))
    if status == model: # 条件を満たした場合カウント -> このやり方でやるのであれば、二重にここに訪れることはできない
        #print('this', seen)
        #cor.add(str(list(seen))) # seen should also includes the one that you did not choose so this is not correct
        #print(bin(status))
        #print('sa')
        ans += 1
    #if len(seen) == M: # "seen" represents how many group have you pocked up and doesn't include when you didn't pick up.
        #return
    m = max(seen)
    for h in range(m, M): # update: avoid to check seen one again, and, "seen" will only include the one you already chosen
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
# this is no need to 全探索
'''
for p in range(M):
    seen = set()
    status = 0
    #jprint(bin(smp[p]))
    #if smp[p] & (1 << 0): # x=1 を含む集合からスタート
        #print(bin(smp[p]))
        #print('yrs')
    status |= smp[p] # 和集合
    seen.add(p) # 確認済み集合
    #print(bin(status))
    dfs(status, seen)
'''

seen = set()
status = 0
seen.add(0) # 確認済み集合
dfs(status, seen)
status |= smp[0] # 和集合
dfs(status, seen)


print(ans)
#print(len(cor))
# why different -> because same value was added to cor
# very complicated and unclear about the definition of "seen" and how you handle it

# status == model で条件を満たした時点でカウントするならば、網羅的に見ていく必要がある。前から順番にたどっていく方法だと、前の方は含まず、後ろの方は含むというケースを考慮できない。
# 一方で、"seen"を、選ぶ選ばないに関わらず見たものとして扱うならば、条件を満たして時点でカウントするというやり方は間違い。全て最後まで、seenした時に初めて条件に合うか検証できる。

# update
# you can imagin a tree for dfs.
# then, if it maches the condition no matter how many node you have, it will increment the ans
