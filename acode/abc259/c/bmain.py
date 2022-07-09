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

while True:
    if T[indexT-1] == T[indexT]:
        if S[indexS-1] != S[indexS]:
            print('No')
            exit()
        else:
            continue
    else:





