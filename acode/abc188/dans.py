#1
N, C = map(int, input().split())
event = []
for i in range(N):
    a, b, c = map(int, input().split())
    a -= 1
    event.append((a, c))
    event.append((b, -c))

event.sort()
ans = 0
fee = 0
t = 0
for x, y in event:
    if x != t:
        ans += min(C, fee) * (x - t)
        t = x
    fee += y

print(ans)

#2
import bisect

N,C=map(int,input().split())
day=set()
a=[]
b=[]
c=[]
for i in range(N):
    aa,bb,cc=map(int,input().split())
    aa-=1
    a.append(aa)
    b.append(bb)
    c.append(cc)
    day.add(aa)
    day.add(bb)
d=list(day)
n=len(d)
dp=[0]*n
d.sort()
for i in range(N):
    k=bisect.bisect_left(d,a[i])
    dp[k]+=c[i]
    k=bisect.bisect_left(d,b[i])
    dp[k]-=c[i]

sum=0
for i in range(1,n):
    dp[i]+=dp[i-1]
for i in range(n-1):
    sum+=min(C,dp[i])*(d[i+1]-d[i])
print(sum)




