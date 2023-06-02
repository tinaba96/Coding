N = int(input())
def seachPrimeNum(n):
    a = list(range(2, n + 1))
    p = list()
    while a[0] ** 2 <= n:
        tmp = a[0]
        p.append(tmp)
        a = [e for e in a if e % tmp != 0]
    return p + a


P = seachPrimeNum(int(N**0.5)+10)

ans=0

for i in range(1,len(P)-1):
    for j in range(i):
        if (P[j]**2)*P[i]*(P[i+1]**2)>N:
            break
        temp = (P[j]**2)*P[i]
        ok=i+1
        ng=len(P)
        # 二分探索
        while abs(ok-ng)>1:
            c=(ok+ng)//2
            if temp*P[c]**2<=N:
                ok=c
            else:
                ng=c
        ans+=ok-i
print(ans)

