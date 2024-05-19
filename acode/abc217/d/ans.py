import bisect
import array
l,q=map(int,input().split())
a=array.array('i',[0,l])
for _ in range(q):
    c,x=map(int,input().split())
    y = bisect.bisect(a,x)
    if c==1:
        a.insert(y,x)
    else:
        print(a[y]-a[y-1])


# https://kanpurin.hatenablog.com/entry/2021/09/05/163703
