N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
import collections
from collections import defaultdict

mp = defaultdict(list)

c = collections.Counter(A)

for i in range(N):
    mp[A[i]].append(i+1)
#print(mp)

for q in range(Q):
   x, k = list(map(int, input().split()))
   if k > c[x]:
       print(-1)
       continue
   else:
       print(mp[x][k-1])




