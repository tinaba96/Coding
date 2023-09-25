from collections import deque
# q=[] # 定数倍により、TLEになる。ただ、考えた方やアルゴリズムは良い。
q=deque()
n=int(input())
s=input()
dl=[]
for i in range(n):
    if s[i]=="(":
        q.append(i)
    if s[i]==")" and q:
        r=q.pop()
        if dl and r<dl[-1][0] and dl[-1][1]<i:
            del dl[-1]
        dl.append((r,i))
b=[True for _ in range(n)]
for i in range(len(dl)):
    for j in range(dl[i][0],dl[i][1]+1):
        b[j]=False
ans=""
for i in range(n):
    if b[i]:
        ans+=s[i]
print(ans)
