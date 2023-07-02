from collections import deque

q=int(input())
mod=998244353 
s=1
d=1
que=deque()
que.append(1)
amari=s%mod

for i in range(q):
    t=list(map(int,input().split()))
    if t[0]==1:
        amari=(amari*10+t[1])%mod
        que.append(t[1])
    elif t[0]==2:
        p=que.popleft()
        #amari=(amari-p*pow(10,d))%mod # 3rd attributes: if you use modular, you can minimize the time complexity
        amari=(amari-p*pow(10,len(que),mod))%mod
    else:
        print(amari)


