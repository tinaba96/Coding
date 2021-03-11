N = int(input())

A = list(map(int, input().split()))

cumsum = []
su = 0
'''
for a in A:
    su += a
    cumsum.append(su)
'''

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        ans += abs(A[i]-A[j])**2
        #print(ans)

print(ans)
#print(cumsum)


