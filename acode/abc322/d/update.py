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

P = []

# 16*4  通り が３つ
def judge(A, B, C):
    for i in range(4):
        for j in range(4):
            if A[i][j] == '#' and B[i][j] == '.' and C[i][j] == '.':
                continue
            if A[i][j] == '.' and B[i][j] == '#' and C[i][j] == '.':
                continue
            if A[i][j] == '.' and B[i][j] == '.' and C[i][j] == '#':
                continue
            return False
    return True

A = [] 
B = [] 
C = [] 

for f in range(4):
    A.append(list(str(input())))
for f in range(4):
    B.append(list(str(input())))
for f in range(4):
    C.append(list(str(input())))

def chFirst(X):
    x = 10
    y = 10
    for i in range(4):
        for j in range(4):
            if X[i][j] == '#':
                x = min(x, j)
                y = min(y, i)
                mx = max(x, j)
                my = max(y, i)
    return x, y, mx-x, my-y # mx-x, my-y is the last index after shifting


nA = [['.' for i in range(4)] for j in range(4)]
nB = [['.' for i in range(4)] for j in range(4)]
nC = [['.' for i in range(4)] for j in range(4)]

def rot1(X):
    nX = [['.' for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            nX[i][j] = X[3-i][3-j]
    return nX

def rot2(X):
    nX = [['.' for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            nX[i][j] = X[3-j][i]
    return nX

def rot3(X):
    nX = [['.' for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            #nX[i][j] = X[3-i][3-j]

            nX[i][j] = X[j][3-i]
            #nX[i][j] = X[i][3-j]
    return nX


def pri(A):
    for i in range(4):
        print(A[i])

'''
pri(A)
A = rot3(A)
print('---')
pri(A)

'''


#def upd(X, nX, a, b):
def upd(X,a, b):
    nX = [['.' for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            if i+b >= 4 or j+a >= 4:
                continue
            nX[i][j] = X[i+b][j+a]
    return nX

def pal(cur, mx, my):
    li = []
    for ni in range(4-mx):
        for nj in range(4-my):
            nxt = [['.' for i in range(4)] for j in range(4)]
            for i in range(4):
                for j in range(4):
                    if i-nj < 0 or j-ni < 0:
                        continue
                    nxt[i][j] = cur[i-nj][j-ni]
            li.append(nxt)
    return li
#print(A) 


aA,bA,mxA,myA = chFirst(A)
nA = upd(A, aA, bA)
pA = pal(nA, mxA, myA)
#print(mxA, myA)
#print(len(pA))

aB,bB,mxB,myB = chFirst(B)
nB = upd(B, aB, bB)
pB = pal(nB, mxB, myB)


aC,bC,mxC,myC = chFirst(C)
nC = upd(C, aC, bC)
pC = pal(nC, mxC, myC)


lA = pA
lB = pB
lC = pC

def op(X):
    aX,bX,mxX,myX = chFirst(X)
    nX = upd(X, aX, bX)
    #print(mxX, myX)
    return pal(nX, mxX, myX)

#print(len(lA))

A1 = rot1(A)
lA += op(A1)
A2 = rot2(A)
lA += op(A2)
A3 = rot3(A)
lA += op(A3)
print('start')
for e in op(A3):
    pri(e)
    print('---')

B1 = rot1(B)
lB += op(B1)
B2 = rot2(B)
lB += op(B2)
B3 = rot3(B)
lB += op(B3)

C1 = rot1(C)
lC += op(C1)
C2 = rot2(C)
lC += op(C2)
C3 = rot3(C)
lC += op(C3)
#print(len(lA))



for a in lA:
    #pri(a)
    #print('----')
    for b in lB:
        for c in lC:
            if judge(a, b, c):
                print('Yes')
                exit()

print('No')

# １つだけWA => 原因不明
# 落ちるケースを探し出せない


