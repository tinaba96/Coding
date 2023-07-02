n,m=map(int,input().split())
s,T=[input()for _ in range(n)],(-1,0,1)
for i in range(n):
    for j in range(m):
        for u in T:
            for v in T:
                A=[(i+t*u,j+t*v)for t in range(5)if n>i+ t*u>=0<=j+ t*v <m]
                if "snuke" == ''.join(s[r][c] for r,c in A):
                    for r,c in A:print(r+1, c+1)
                    exit()
