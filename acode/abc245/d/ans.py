n,m=map(int,input().split())
n+=1
m+=1
a=list(map(int,input().split()))[::-1]
c=list(map(int,input().split()))[::-1]
b=[0]*(m)
#print(a)
#print(c)

for i in range(m):
    d=c[i]//a[0]
    b[i]=d
    for j in range(n):
        c[i+j]-=d*a[j]
    #print(c)
    #print(b)
    #print()

print(*b[::-1])


