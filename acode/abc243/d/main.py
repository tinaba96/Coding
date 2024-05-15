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
    # binary search if cntU < cntL+cntR
    print(i)

# O(NlogN)
# if cntU == cntL+cntR
# should be same position

# if cntU > cntL+cntR
# devide number of node in current level with number of node in taget level. quotient will be the position of the node in target level


print(cntU)
print(cntL+cntR)
p = int(x)+cntR+cntL-cntU
val = 2**(cntR+cntL-cntU)
print(ini*val + 2**p)


