import sys
sys.setrecursionlimit(500005)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

N, X, Y = list(map(int, input().split()))

mp = [[] for i in range(N+1)]

for i in range(N-1):
    u, v = list(map(int, input().split()))
    mp[u].append(v)
    mp[v].append(u)


seen = set()

seen.add(str(X))
ans = [X]

def count(ans, seen):
    for k in range(len(mp[ans[-1]])):
        if str(mp[ans[-1]][k]) in seen:
            continue
        if mp[ans[-1]][k] == Y:
            ans.append(Y)
            print(*ans)
            exit()
        ans.append(mp[ans[-1]][k])
        seen.add(str(mp[ans[-2]][k]))
        count(ans, seen)
        p = ans.pop()
        seen.remove(str(p))
        #seen.remove(str(mp[ans[-1]][k]))

count(ans, seen)


# by using set and sys.setrecursionlimit, it became AC
# the reason for RE is the limit of recursion

# Since the recursion for pypy is very slow, this will be TLE for pypy where as python will be AC
# However if you use pypyjit/set_param for pypy it will be AC
# https://qiita.com/shoji9x9/items/e7d19bd6f54e960f46be

'''
pythonの再帰はやっぱり遅いですよね、、
再帰制限は頭に入れてなかったの助かりました。
@うい さん、ありがとうございました。

いや、再帰が遅いのはPythonよりもPypyだよ

確かにset使ってpythonで提出したらACしました！
pypyの再起が遅いのはどうしてでしょうか。
JITコンパイルを使っているpypyであれば、一回呼ばれた関数は早く処理できそうな勝手なイメージがありました。

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
これつけると少し早くなる（ループ展開する再帰関数部分の上限がなくなる）

https://qiita.com/shoji9x9/items/e7d19bd6f54e960f46be
これが詳しいよ

お二方ともありがとうございます！
確かに上記をつけるとPypyでもACしました。
ざっくりとしたイメージとしては、
pypyの方がJITにより基本的には高速になるが、再帰においてはJITがあまり活かせれておらず（有効になっていない？）、JITのパラメータをいじることで再帰においても高速化できると言ったとこですかね。

ざっくりとしたイメージというより、まさにその通りたと思います

ありがとうございます！非常に勉強になりました！
'''

