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

mp = [[] for m in range(N+1)]


for i in range(M):
    u, v = list(map(int, input().split()))
    mp[u].append(v)
    mp[v].append(u)

#print(mp)
ind = 1
if len(mp[ind]) >= 3:
    print('No')
    exit()
if len(mp[ind]) == 0:
    print('No')
    exit()

al = set()
al.add(ind)
sind1 = set()
ind1 = mp[ind][0]
al.add(ind1)
while True:
    #print(ind1)
    if len(mp[ind1]) == 0 or len(mp[ind1]) >= 3:
        print('No')
        exit()
    if ind not in mp[ind1]:
        print('No')
        exit()
    if len(mp[ind1]) == 1:
        break
    if ind == mp[ind1][0]:
        ind = ind1
        ind1 = mp[ind1][1]
    else:
        ind = ind1
        ind1 = mp[ind1][0]
    if ind1 not in sind1:
        sind1.add(ind1)
        al.add(ind1)
    else:
        print('No')
        exit()
    #print(ind1)
        
ind = 1
if len(mp[ind]) == 2:
    ind2 = mp[ind][1]
    al.add(ind2)
sind2 = set()

if len(mp[ind]) == 2:
    while True:
        if len(mp[ind2]) == 0 or len(mp[ind2]) >= 3 or ind not in mp[ind2]:
            print('No')
            exit()
        if len(mp[ind2]) == 1:
            break
        if ind == mp[ind2][0]:
            ind = ind2
            ind2 = mp[ind2][1]
        else:
            ind = ind2
            ind2 = mp[ind2][0]
        if ind2 not in sind2:
            sind2.add(ind2)
            al.add(ind2)
        else:
            print('No')
            exit()

if len(al) == N:
    print('Yes')
else:
    print('No')
