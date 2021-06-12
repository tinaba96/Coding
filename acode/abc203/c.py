N, K = list(map(int, input().split()))

m = {}

for n in range(N):
    A, B = list(map(int, input().split()))
    if A in m:
        m[A] += B
    else:
        m[A] = B

sortedm = sorted(m.items())
#print(sortedm)

#print(len(sortedm))
for e in range(len(sortedm)):
    if int(sortedm[e][0]) <= K:
        K += sortedm[e][1]

if K < 10**100:
    print(K)
else:
    print(10**100)
#print(mon)




