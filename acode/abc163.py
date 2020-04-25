'''
#A
pi4 = 0
for i in range(1000000):
    pi4 += (1 / (i * 4 + 1) - 1 / (i * 4 + 3))
pi = pi4 * 4    # 3.141592153589902

R = int(input())

print(2*pi*R)

#pi = acos(-1)を利用しても良い。

#B
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

if N < sum(A):
    print(-1)
else:
    print(N-sum(A))


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
'''

#解説：最小値で選んだk個と最大値で選んだk個において、それそれ対応する項ごとに差をとると、n-k+1がk項出てくる。よって、k(n-k+1)+1が解になり、2乗の和の公式などをk~n+1において使用すれば、O(1)でこの問題を解くことができる。


#Dans
N, K = map(int, input().split())
mod = 1000000007

ans = 0

for i in range(K, N + 2):
    min_candidate = ((i - 1) * i * (1/2)) % mod
    max_candidate = ((2 * N + 1 - i) * i * (1/2)) % mod #初項N-i、末項N+1数列がi個ある。
    ans = ans + (max_candidate - min_candidate + 1) 
print(int(ans % mod)) #//を使ってない分intで整数に直している。

#計算上少数が生じることはないので、//やint()は必要ないと思われる。
#しかし、.0と、少数まで表示されてしまうため、上記は結局必要
#理由は、割り算の計算(/)をすると、少数まで表示されるようになっているから。
'''

#another
N, K = map(int, input().split())

ans = 0
MOD = 10**9 + 7


def sum(a, b):
    return (b - a + 1) * (a + b) // 2


for i in range(K, N + 2):
    min = sum(0, i - 1)
    max = sum(N - (i - 1), N)
    ans += max - min + 1

print(ans % MOD)


#another
def my_code_D():
    mod = 10**9+7
    n,k = map(int, input().split())
    res = 0
    for i in range(k,n+1):
        count = (n*i - i*(i-1) + 1)%mod
        res = (res + count)%mod
    res = (res+1)%mod # +1はk=N+1の文である。N+1の場合常に1通りであるため。
    print(res)

my_code_D()

'''
