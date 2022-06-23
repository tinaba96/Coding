import bisect

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

mi = min(A)
ma = max(A)

tot = sum(A)

sortA = sorted(A)
#print(sortA)

cul = [0 for i in range(N)]

tmp = 0
for i in range(N):
    tmp += sortA[i]
    cul[i] = tmp

#print(cul)

for _ in range(Q):
    q = int(input())
    if q <= mi:c # this is needed because it becomes cul[-1] if index=0. it should be 0 and you dont need these conditions
        print(abs(N*q-tot))
    elif ma <= q:
        print(abs(N*q-tot))
    else:
        index = bisect.bisect_right(sortA, q)
        index2 = bisect.bisect_left(sortA, q)
        #print('index', index, ':', index2)
        rval = cul[-1] - cul[index-1]
        lval = cul[index2-1]
        val = rval-q*(N-index)
        val2 = q*index2 - lval
        #print(val2)
        print(val+val2)




    


