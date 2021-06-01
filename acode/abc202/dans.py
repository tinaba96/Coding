import math
def C(n,r):return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
A,B,K=map(int,input().split())
ans=''

for i in range(A+B-1):  # because of the factorial(), it should be A+B > 1
    if A==0 or B==0: c=1  # because of the factorial()
    else: c=C(A+B-1,B)

    if K <= c and A:
        ans+='a'
        A-=1
    else:
        ans+='b'
        B-=1
        K-=c

print(ans + ('a' if A==1 else 'b'))

