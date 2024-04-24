N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
ans = []
for t in range(N):
    ans.append(T[t])

clk = 0

index_min = T.index(min(T))

ns = S[index_min:] + S[:index_min]
nt = T[index_min:] + T[:index_min]

#if nt[0] < ans[0]:
#    ans[0] = nt[0]

pos = N - index_min 

for n in range(N-1):
    if n < pos:
        k = n + index_min
    else:
        k = n - pos
    if nt[n]+ns[n] < nt[n+1]:
        if n == pos-1:
            ans[0] = nt[n]+ns[n]
        else:
            ans[k+1] = nt[n]+ns[n]
        nt[n+1] = nt[n]+ns[n]
        #print(ans)


[print(i) for i in ans]
        


