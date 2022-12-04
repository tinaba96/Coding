import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

S = []
T = []

H, W = list(map(int, input().split()))

for i in range(H):
    s = str(input())
    S.append(s)
for j in range(H):
    t = str(input())
    T.append(t)

#print(S)

from collections import defaultdict
dox = defaultdict(int) 
#dox = dict()
#dox2 = defaultdict(int)

for a in range(W):
    tmp = ''
    for b in range(H):
        tmp += S[b][a]
    #if tmp in dox:
    tmp = int(tmp.replace('#', '1').replace('.', '0'), base=2)
    dox[tmp] += 1
    #else:
    #    dox[tmp] = 1


#print(box)

for e in range(W):
    tmp2 = ''
    for z in range(H):
        tmp2 += T[z][e]
    #if tmp2 not in dox:
    #    print('No')
    #    exit()
    tmp2 = int(tmp2.replace('#', '1').replace('.', '0'), base=2)
    dox[tmp2] -= 1
    if dox[tmp2] < 0:
        print('No')
        exit()
#print(dox
#print(dox2)
print('Yes')
#print('Yes' if len(dox) == 0 else 'No')
#print('Yes' if dox == dox2 else 'No')
'''
if len(box) == 0:
    print('Yes')
else:
    print('No')

'''

# Pypy3: TLE
# Python3: AC

