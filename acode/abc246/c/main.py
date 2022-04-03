N, K, X = list(map(int, input().split()))
A = list(map(int, input().split()))

new = []
su = sum(A)
cnt = 0
for i in range(N):
    if A[i] >= X:
        cnt += 1
if cnt >= K:
    print(su - K*X)
    exit()

cnt = 0
for i in range(N):
    if A[i] >= X:
        cnt += A[i] // X
        A[i] = A[i] % X

if cnt >= K:
    print(su - K*X)
    exit()
else:
    ans = cnt*X

#print('a', su-ans)

left = K - cnt
#print(left)

A.sort(reverse=True)

# print(A)

p = 0

if left > N:
    print(0)
    exit()

for i in range(left):
    p += A[i]

#print(su)
#print(ans)
print(su - ans-p)


