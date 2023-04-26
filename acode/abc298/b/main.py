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


N = int(input())
A = []
B = []

for i in range(N):
    tmp = list(map(int, input().split()))
    A.append(tmp)

for i in range(N):
    tmp = list(map(int, input().split()))
    B.append(tmp)

ans = True
for z in range(N):
    for x in range(N):
        if A[z][x] == 1:
            if B[z][x] != 1:
                ans = False

new = [[0 for p in range(N)] for q in range(N)]
for i in range(N):
    for j in range(N):
        new[j][N-1-i] = A[i][j]

ans2 = True
for z in range(N):
    for x in range(N):
        if new[z][x] == 1:
            if B[z][x] != 1:
                ans2 = False


new2 = [[0 for p in range(N)] for q in range(N)]
for i in range(N):
    for j in range(N):
        new2[j][N-1-i] = new[i][j]
        #new2[N-j-1][i] = new[i][j]

ans3 = True
for z in range(N):
    for x in range(N):
        if new2[z][x] == 1:
            if B[z][x] != 1:
                ans3 = False


#print(new2)
new3 = [[0 for p in range(N)] for q in range(N)]
for i in range(N):
    for j in range(N):
        new3[j][N-1-i] = new2[i][j]
ans4 = True
for z in range(N):
    for x in range(N):
        if new3[z][x] == 1:
            if B[z][x] != 1:
                ans4 = False

if ans or ans2 or ans3 or ans4:
    print('Yes')
else:
    print('No')
