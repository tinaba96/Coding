S = str(input())
T = str(input())

if len(T) < len(S):
    print('No')
    exit()

l = min(len(T), len(S))
if S[0] != T[0]:
    print('No')
    exit()

indexS = 1
indexT = 1
cntS = 1
cntT = 1

while True:
    while S[indexS-1] == S[indexS]:
        cntS += 1
        indexS += 1
        if indexS == len(S):
            break
    while T[indexT-1] == T[indexT]:
        cntT += 1
        if indexT+1 == len(T):
            break
        indexT += 1


    if T[indexT-1] != S[indexS-1]:
        print('No')
        exit()
    if T[indexT-1] == S[indexS-1] and cntT >= 2 and cntS < 2 and cntT >= cntS:
        print('No')
        exit()
    if T[indexT-1] == S[indexS-1] and cntS >= 2 and cntT < cntS:
        print('No')
        exit()

    indexS += 1
    indexT += 1


    if indexS > len(S)-1:
        break
    if indexT > len(T)-1:
        break
    cntT = 1
    cntS = 1
#print(S[-1])
#print(T[indexS-1])
if T[indexT-1] != S[-1]:
    print('No')
    exit()


if len(T) > len(S) and T[indexT-1] == S[-1]:

    if cntS <= 1 and cntT > 1:
        print('No')
        exit()
    for t in range(indexT-1, len(T)):
        if T[t] != S[-1]:
            print('No')
            exit()

print('Yes')





