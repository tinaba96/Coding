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


N, M = list(map(int, input().split()))
L = list(map(int, input().split()))

# dp
#print(sum(L))
mini = sum(L)//M
#print(mini)

cumsum = []
tmp = 0
for l in L:
    cumsum.append(tmp+l)
    tmp += l+1

print(cumsum)
import bisect

def ch(ind):
    arr = cumsum
    cnt = 0
    v = ind
    while True:
        cnt += 1
        if cnt > M:
            return False
        g = bisect.bisect_right(arr, v)
        arr = arr[g:]

        if len(arr) == 0:
            return False

        v = ind+arr[0]-1
        print(cnt)
        print(arr)
        
        if v > cumsum[-1]:
            return True


print(ch(24))


# 二分探索を使って求めらると思ったが、今の状態だと空白がうまく扱えていない
# 空白も入れてcumsumを考えるとどこから単語がスタートするか分からない

