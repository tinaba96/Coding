def get():
    return [int(i) for i in input().split()]
a=list(input())
import itertools
p=itertools.permutations
ss=p(a)

ans=-10

for i in list(ss):
    lis=i
    for i in range(1,len(a)):
        x="".join(lis[:i])
        y="".join(lis[i:])
        #print(x,y)
        x=int(x)
        y=int(y)
        ans=max(ans,x*y)
print(ans)


