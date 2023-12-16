S = list(map(int, input().split()))

v = S[0]
if v%25 != 0 or v > 675 or 100 > v:
    print('No')
    exit()

for i in range(1, len(S)):
    if S[i] < v or S[i]%25 != 0 or S[i] > 675 or 100 > S[i]:
        print('No')
        exit()
    else:
        v = S[i]



print('Yes')



