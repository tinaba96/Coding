N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0
for i in range(M):
    ans += (i+1)*A[i]

cum = []
c = 0
for p in range(N):
    c += A[p]
    cum.append(c)
    
#print(cum)


l = 0
r = M-1
val = ans
for k in range(N-M):
    #print(val)
    val -= A[l]
    val -= cum[r]-cum[l]
    #print(val)
    l += 1
    r += 1
    val += M*A[r]
    ans = max(ans, val)







print(ans)


