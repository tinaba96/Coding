n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())

#for i in range(p-1,q):
for i in range(p,q+1):
    rowa  = ""
    #for j in range(r-1,s):
    for j in range(r,s+1):
        #if abs(i+1-a) == abs(b-j-1) :
        if (i-j)==(a-b) or (i+j)==(a+b):
            rowa += "#"
        else:
            rowa += "."
    print(rowa)

