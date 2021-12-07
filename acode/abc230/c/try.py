
n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())

for i in range(p-1,q):
    rowa  = ""
    for j in range(r-1,s):
        if abs(i+1-a) == abs(b-j-1) :
            rowa += "#"
        else:
            rowa += "."
    print(rowa)
