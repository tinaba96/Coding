A = list(map(int, input().split()))

mp =set()

import collections

for i in A:
    mp.add(i)

c = collections.Counter(A)

if len(c) == 2 and (c[A[0]] == 2 or c[A[0]] == 3):
    print('Yes')
else:
    print('No')



