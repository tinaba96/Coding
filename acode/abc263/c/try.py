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
    #print(*v)
ans = sorted(m)
print(m)
print(ans)
#print(ans)

