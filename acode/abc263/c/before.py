N, M = list(map(int, input().split()))

import itertools

l = []

for i in range(M):
    l.append(str(i+1))

#if N == 1:



m = []
for v in itertools.combinations(l, N):
    #print(sorted(list(v)))
    m.append(int(''.join(v)))
    #print(int(*v))
ans = sorted(m)
print(ans)

for k in (ans):
    k = str(k)
    #print(*[k[a] for a in range(N)])
    an = [k[0]]
    flag = True
    for a in range(len(k)-1):
        if k[a+1] == '0':
            an.append(k[a+1])
            continue
        if k[a] >= k[a+1]:
            flag = False
            break
        else:
            an.append(k[a+1])
    if flag:
        print(*an)



