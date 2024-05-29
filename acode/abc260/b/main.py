N, X, Y, Z = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AA = []
BB = []
C = []
CC = []
for i in range(N):
    C.append(A[i]+B[i])

for i in range(N):
    AA.append([i, A[i]])
    BB.append((i, B[i]))
    CC.append((i, C[i]))


AA = sorted(AA, key=lambda x: x[1], reverse=True)
BB = sorted(BB, key=lambda x: x[1], reverse=True)
CC = sorted(CC, key=lambda x: x[1], reverse=True)

As = sorted(A)
As = As[::-1]
scoreA = AA[:X]

check = set()

cntA = 0
cntB = 0
cntC = 0

ans = []

for e in scoreA:
    if cntA == X:
        break
    check.add(e[0]+1)
    cntA += 1
    ans.append(e[0]+1)


Bs = sorted(B)
Bs = Bs[::-1]
scoreB = BB[:Y]

for eb in BB:
    if cntB == Y:
        break
    if eb[0]+1 in check:
        continue
    else:
        check.add(eb[0]+1)
        cntB += 1
        ans.append(eb[0]+1)



Cs = sorted(C)
Cs = Cs[::-1]
scoreC = CC[:Z]

for ec in CC:
    if cntC == Z:
        break
    if ec[0]+1 in check:
        continue
    else:
        check.add(ec[0]+1)
        cntC += 1
        ans.append(ec[0]+1)


ans.sort()

for i in range(len(ans)):
    print(ans[i])
