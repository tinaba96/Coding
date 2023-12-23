import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict
#d = defaultdict(int)


N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

if K == 1:
    print(0)
    exit()

ans = 0
if K%2 == 0:
    for i in range(0, K, 2):
        ans += A[i+1]-A[i]

    print(ans)
    exit()


base = 0
for i in range(0, K-1, 2):
    base += A[i+1]-A[i]

print(base)


mid = K // 2


left = 0
right = 0

for i in range(1, mid, 2):
    left += A[i]-A[i-1]


for i in range(mid+1, K, 2):
    right += A[i]-A[i-1]

# 除くidを基準にleftとrightの合計を計算しておき、除くidを徐々にずらしていく。
# 最終的に合計の最小値を求める。

    
