from collections import *
f=lambda:map(int,input().split())
n,m=f()
s=[0,*f()]
x=[*f()]
for i in range(n-1):s[i+1]-=s[i] # see the formula explained in video tutorial
d=Counter()
e=1
for i in s:
  for j in x:d[e*(j-i)]+=1
  e*=-1
print(max(d.values()))

