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

A = []
B = []
C = []

Ha, Wa = list(map(int, input().split()))
for i in range(Ha):
    A.append(str(input()))
Hb, Wb = list(map(int, input().split()))
for i in range(Hb):
    B.append(str(input()))
Hx, Wx = list(map(int, input().split()))
for i in range(Hx):
    X.append(str(input()))

ans = 'No'

tara = []
tarb = []
tarx = []

chex = set()

for i in range(Ha):
    for j in range(Wa):
        if A[i][j] == '#':
            tara.append((i, j))

for i in range(Hb):
    for j in range(Wb):
        if B[i][j] == '#':
            tarb.append((i, j))
for i in range(Hx):
    for j in range(Wx):
        if X[i][j] == '#':
            tarx.append((i, j))
            chex.add((i, j))


for i in range(len(tarx)):
    x = tarx[i][0]
    y = tarx[i][1]
    for j in range(len(tara)):
        xa = tara[i][0]
        ya = tara[i][1]
        dx = x - xa
        dy = y - xy
        f = True
        for c in range(len(tara)):
            cx = tarax[c][0]
            cy = tarax[c][1]
            if tara[cx+dx][cy+dy] not in chex:
                f = False
                break




