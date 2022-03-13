import math

N, X = list(map(int, input().split()))
S = str(input())

cntU = 0
cntL = 0
cntR = 0

x = math.log(X,2)
#print(x)
ini = X-2**26

LR = []

for i in range(len(S)):
    if S[i] == 'U':
        cntU += 1
    if S[i] == 'L':
        LR.append('L')
        cntL += 1
    if S[i] == 'R':
        LR.append('R')
        cntR += 1

for i in range(len(LR)):




print(cntL)
print(cntR)
p = int(x)+cntR+cntL-cntU
val = 2**(cntR+cntL-cntU)
print(ini*val + 2**p)


