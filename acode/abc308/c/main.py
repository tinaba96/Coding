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

li = []

N = int(input())
for i in range(N):
    A, B = list(map(int, input().split()))
    li.append([i+1, A, B])


def compare(I1, A1, B1, I2, A2, B2): # I no need
    v1 = A1*(A2+B2)
    v2 = A2*(A1+B1)
    if v1 >= v2: # check = is needed or not
        return True
    else:
        return False

# どうやって比較関数を使うのか？

# 配列aを昇順に並べ替える
def merge_sort(a):
    if len(a) == 1:
        return

    # 配列を二つに分ける
    m = len(a) // 2
    x = a[:m]
    y = a[m:]

    # 分割とマージを再帰的に行う。最終的に一つの要素まで分割された段階からマージが行われていく
    merge_sort(x)
    merge_sort(y)
    merge(x, y, a)

# 配列x, yをマージし、aにセットする
def merge(x, y, a):
    # x, yのindex
    i = 0
    j = 0

    #print(y)
    #print('x : ', x[0][0], x[1])

    # x, yの先頭の要素を比較し、小さい要素から順にaにセットしていく
    while i < len(x) or j < len(y):
        # xの要素を全て追加済みの場合、y[j]をセットする
        if i == len(x):
            a[i+j] = y[j]
            j += 1
        # yの要素を全て追加済みの場合、x[i]をセットする
        elif j == len(y):
            a[i+j] = x[i]
            i += 1
        # x[i]がy[j]以下の場合、x[i]をセットする
        #elif x[i][0] <= y[j][0]:
        elif compare(x[i][0], x[i][1], x[i][2], y[j][0], y[j][1], y[j][2]):
            #print('cs')
            a[i+j] = x[i]
            i += 1
        # y[j]がx[i]より小さい場合、y[j]をセットする
        else:
            a[i+j] = y[j]
            j += 1

#print(li)
merge_sort(li)

ans = []
for i in range(len(li)):
    ans.append(li[i][0])
    #print(li[i][0])

print(*ans)
