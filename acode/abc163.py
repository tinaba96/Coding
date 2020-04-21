'''
#A
pi4 = 0
for i in range(1000000):
    pi4 += (1 / (i * 4 + 1) - 1 / (i * 4 + 3))
pi = pi4 * 4    # 3.141592153589902

R = int(input())

print(2*pi*R)
#B
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

if N < sum(A):
    print(-1)
else:
    print(N-sum(A))
'''
#C
import collections
N = int(input())
c = []
A = list(map(int, input().split()))
cnt = collections.Counter(A)
for i in range(1, N+1):
    print(cnt[i])

#D
#unratedになったのでideaだけ簡単に
N, K = list(map(int, input().split()))
ans = 0
memo = {}
arr = []
for i in range(N+1):
    arr.append(10**100 + i)

def count(N, K):
    if memo[k] != "":
        memo[k] = comb(N, K)
    ans += memo[k]
    if K == N:
        return ans
    else:
        cont(N, K+1)

count(N, K)
print(ans%(10**9+7))




