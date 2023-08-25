from fractions import Fraction
N,M =map(int,input().split())
R = []
for i in range(N):
    C,P,*S = map(Fraction,input().split())
    tmp = []
    z = 0
    for s in S:
        if s == 0:
            z += 1
        else:
            tmp.append(int(s))
    R.append((C,P,tmp,z))
DP = [-1]*(M+1)
DP[-1] = 0
for i in range(M-1,-1,-1):
    res = 10**18
    for j in range(N):
        tmp = 0
        C,P,S,zero = R[j] # zero: number of zero
        for s in S: 
            if i+s >= M+1: # when the score is enough to be more than M
                tmp += C*P/(P-zero)/(P-zero)
            else:
                tmp += (C*P/(P-zero)+DP[i+s])/(P-zero)
        res = min(res,tmp)
    DP[i] = res
print(float(DP[0]))


