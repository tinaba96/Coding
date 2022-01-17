#priority queue

from heapq import heapify, heappop, heappush
n, k = map(int, input().split())
p = list(map(int, input().split()))

cp = p[:k]
print(min(cp))
heapify(cp)

for i in range(k,n):
    mn = heappop(cp)
    mn = max(mn,p[i])
    heappush(cp,mn)
    res = heappop(cp)
    print(res)
    heappush(cp,res)



