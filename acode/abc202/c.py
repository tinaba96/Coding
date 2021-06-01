import collections

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

cntA = collections.Counter(A)
cntB = collections.Counter(B)
cntC = collections.Counter(C)

#bCount =  []
#for x in range(1,N+1):
#    bCount.append(cntC[x])

#print('bcnt: ', bCount)
ans = 0

#for i in range(1, N+1):
#    for j in range(N):
#        if i == B[j]:
#            ans += cntA[i]*bCount[j]

for i in range(N): # B loop
        #ans += cntA[i]*cntC[i]*min(1, cntB[C[i]])
        ans += cntA[B[i]]*cntC[i+1]
        #print(ans)

print(ans)

# it is depending ton which variable you focus on.
# i focussed on the index of B but the snuke focusses on the index of C
# my approach is a little bit complicated
# cntA[B[C[i]-1]] is easier to understand which is a snuke's approach



