import sys
sys.setrecursionlimit(10**8)
N,Q = map(int,input().split())
roads = [[]for _ in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    a -=1
    b -=1
    roads[a].append(b)
    roads[b].append(a)

dist = [-1]*N
dist[0] = 0
def count_dist(i):
    for j in roads[i]:
        if dist[j] ==-1:
            dist[j] = dist[i]+1
            count_dist(j)
    return
count_dist(0)

for i in range(Q):
    c,d = map(int,input().split())
    c -=1
    d -=1
    if (dist[c]+dist[d])%2 == 0:
        print("Town")
    else:
        print("Road")

# 参考
# https://yunix-kyopro.hatenablog.com/entry/2021/07/11/020240?_ga=2.121161536.9506465.1625937519-1301098457.1625937519
#クエリのたびに距離をBFSなどで求めていては計算量がO(NQ)になってしまい、間に合いません。
