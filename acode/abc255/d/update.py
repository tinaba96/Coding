import bisect

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

mi = min(A)
ma = max(A)

tot = sum(A)

sortA = sorted(A)
#print(sortA)

cul = [0 for i in range(N+1)]

tmp = 0
for i in range(N):
    tmp += sortA[i]
    cul[i+1] = tmp

#print(cul)

for _ in range(Q):
    q = int(input())
    index = bisect.bisect_right(sortA, q)
    rval = cul[-1] - cul[index]
    lval = cul[index]
    val = rval-q*(N-index)
    val2 = q*index - lval
    #print(val2)
    print(val+val2)




    


