<h1>This is the techniques which I learned so far<h2>
<br>

## **map関数**

```
list(map(関数,  イテラブル))
```

- イテラブルとはlistやrange関数のようなfor文のinの後に書けるオブジェクトです。
- イテラブルのすべての要素に第1引数で設定した関数を適応させることができます。

<br>

## **いもす法**

- いもす法とは，累積和のアルゴリズムを多次元，多次数に拡張したものです．

<br>

参考URL：https://imoz.jp/algorithms/imos_method.html

<br>

## **ライブラリ（bisect）**

- Pythonのlistのソートの平均時間計算量はO(nlog⁡n)である。
- そこで、ソートされたリストに対してソート順序を保ったまま値を挿入したい場合、わざわざappendしてsortしているとパフォーマンスはよくない。
- そのような場面で役立つのがこの「bisect」である。
<br>

- bisectには挿入箇所を探索する関数(bisect)と探索と挿入を同時に行う(insort)の主に２つの関数が存在する。

例：
```
bisect.bisect_left(a, x, lo=0, h=len(a))
```

a: ソート済みリスト
x: 挿入したい値
lo: 探索範囲の下限
hi: 探索範囲の上限
(lo, hiはスライスと同様の指定方法)


```
A = [1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
print(A)
index = bisect.bisect_left(A, 3) # 2 最も左(前)の挿入箇所が返ってきている
A.insert(index, 3)
print(A) # [1, 2, 3, 3, 3, 3, 4, 4, 6, 6, 6, 6]

# 探索範囲を絞り込む
A = [1, 2, 3, 3, 3, 0, 0, 0, 0, 0, 0]
index = bisect.bisect_left(A, 3, 0, 5)
print(index)# 2
```


参考URL：https://qiita.com/ta7uw/items/d6d8f0ddb215c3677cd3




## Pythonの文字列

- 文字列はイミュータブル（変更できない）ため、文字の置き換えはできない。

  例）
  ```
  (S[:n], S[n:]) = S([n:], S[:n])
  ```


## **ライブラリ（deque）**

- リストの削除などが、O(1)で行えるデータ構造。

## **ライブラリ（collections.Counter）**

- リストの値の出現回数を持つ辞書型dictのサブクラス。

例）
```
import collections

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

c = collections.Counter(l)
print(c)
# Counter({'a': 4, 'c': 2, 'b': 1})

print(type(c))
# <class 'collections.Counter'>

print(issubclass(type(c), dict))
# True
```

## 平均計算量と償却計算量（ならし計算量）の違い

- 似たものとして平均計算量というものがあります。これは全ての入力パターンの平均をとったものです。償却計算量とのちがいは独立に行った時の平均をとるか、連続して行った時の平均をとるかです。


## **ライブラリ(itertools.product())

- 直積（デカルト積）は、複数の集合から要素を一つずつ取り出した組み合わせの集合。

例（使い方））

```
import itertools
import pprint

l1 = ['a', 'b', 'c']
l2 = ['X', 'Y', 'Z']

p = itertools.product(l1, l2)

print(p)
# <itertools.product object at 0x1026edd80>

print(type(p))
# <class 'itertools.product'>

for v in p:
    print(v)
# ('a', 'X')
# ('a', 'Y')
# ('a', 'Z')
# ('b', 'X')
# ('b', 'Y')
# ('b', 'Z')
# ('c', 'X')
# ('c', 'Y')
# ('c', 'Z')

for v in p:
    print(v)

for v1, v2 in itertools.product(l1, l2):
    print(v1, v2)
# a X
# a Y
# a Z
# b X
# b Y
# b Z
# c X
# c Y
# c Z

```

## pythonでのアスタリスク*

```
my_list = [1, 2, 3]
print(*my_list)

# 実行結果
# 1 2 3
```


## ならし計算量
- 一回あたりの計算量ではなく、全体的な合計の計算量　（参照：abc189C）


## unionfind


# 基本的にはPython3よりもPypy3のほうが早い

- 場合によってはPypy3のほうが遅いテストケースもあるが、全体的にはPypy3の方が早い場合が圧倒的に多い。
- https://qiita.com/OKCH3COOH/items/f0c5c4681bc30dddf7f4


## tupleの配列のsort（key指定あり）

```
a = [(3,3), (2,2), (3,1), (4,2)]
a.sort(key=lambda x: x[0])
print(a) # => [(2, 2), (3, 3), (3, 1), (4, 2)]
```

## ２次元累積話

おそらく参考になるサイト
https://qiita.com/drken/items/56a6b68edef8fc605821

- abc203 D


## Union Find

- https://note.nkmk.me/python-union-find/

```
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
```
`uf = UnionFind(6)`
  
```
class DSU:
    def __init__(self, n):
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        x, y = self.leader(a), self.leader(b)
        if x == y: return x
        if -self.parent_or_size[x] < -self.parent_or_size[y]: x, y = y, x
        self.parent_or_size[Fjx] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        assert 0 <= a < self._n
        if self.parent_or_size[a] < 0: return a
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a):
        assert 0 <= a < self._n
        return -self.parent_or_size[self.leader(a)]

    def groups(self):
        leader_buf = [self.leader(i) for i in range(self._n)]
        result = [[] for _ in range(self._n)]
        for i in range(self._n): result[leader_buf[i]].append(i)
        return [r for r in result if r != []]
```

- 「プロコン攻略ガイド」参考

## ワーシャルフロイド法

- ありほん
- abc208D




## 複素数

参考
- https://note.nkmk.me/python-complex/

偏角（ソート）
- https://techacademy.jp/magazine/32436
- https://qiita.com/ganyariya/items/adef1a7f89ae88b804da
  


## Python int型について

- intz型に下限上限はない
- https://note.nkmk.me/python-int-max-value/
  

## ILP32 と LP64 データ・モデルおよびデータ型サイズ

- https://www.ibm.com/docs/ja/zos/2.3.0?topic=environments-ilp32-lp64-data-models-data-type-sizes
  

  ## ヒープキューアルゴリズム　（優先度キューまたはpriority queue）　heapq

- heapq.heappush(heap, item)
item を heap に push します。ヒープ不変式を保ちます。

- heapq.heappop(heap)
pop を行い、 heap から最小の要素を返します。ヒープ不変式は保たれます。ヒープが空の場合、 IndexError が送出されます。pop せずに最小の要素にアクセスするには、 heap[0] を使ってください。

- heapq.heappushpop(heap, item)
item を heap に push した後、pop を行って heap から最初の要素を返します。この一続きの動作を heappush() に引き続いて heappop() を別々に呼び出すよりも効率的に実行します。

- heapq.heapify(x)
リスト x をインプレース処理し、線形時間でヒープに変換します。

- 参考
https://docs.python.org/ja/3/library/heapq.html
https://qiita.com/Kept1994/items/a28cddecd56a07ef4d14


## python 再帰の限界
- デフォルトは1000回（深さ）
- どんなに軽い再起でも1000回以上はエラーを吐く
- しかし、増やすことはできる。

```
import sys
#import resource

sys.setrecursionlimit(4000)
#print(sys.getrecursionlimit())
# naximum recursion is 1000
```

## DFS
- 応用　abc213E
- 


## BFS
- 復習 abc224D

## DP
- 復習 abc220D
- https://atcoder.jp/contests/dp

## itertools.permutation

- 文字列の順列を列挙したい時など
- 辞書順に並び替えをする問題など
- もちろん文字列であれは数値も可能
- 結構遅い。長さ20は無理で、8くらいならOK?
- ABC215C
- Typical90-002ではTLEしてしまった。かなり遅い。正確なオーダーを知りたい。


```
import itertools

l = ['a', 'b', 'c', 'd']

p = itertools.permutations(l, 2)

print(type(p))
# <class 'itertools.permutations'>
for v in itertools.permutations(l, 2):
    print(v)
# ('a', 'b')
# ('a', 'c')
# ('a', 'd')
# ('b', 'a')
# ('b', 'c')
# ('b', 'd')
# ('c', 'a')
# ('c', 'b')
# ('c', 'd')
# ('d', 'a')
# ('d', 'b')
# ('d', 'c')
```

## 三角関数
- ```from math import atan2, cos, pi, sin, sqrt, degrees```
- 参考
  https://note.nkmk.me/python-math-sin-cos-tan/
- TYP 018
  https://atcoder.jp/contests/typical90/tasks/typical90_r

  ## gcd
  - 計算量　O(log min(x, y))

割って余りを取るという操作を、最悪でも小さい方の十進法での桁数の約 5 倍繰り返せば、最大公約数に達する（ラメの定理）。

最大公約数を求めるのに、素因数分解してみればいいと考える人がいるかもしれないが、この定理は素因数分解を用いるよりもユークリッドの互除法による方がはるかに速いということを述べている。

実際、計算複雑性理論においては最大公約数を求めることは「容易な問題」として知られており、素因数分解は「困難な問題」であろうと考えられている。 入力された2つの整数のうち小さいほうの整数 n の桁数を d とすれば、ユークリッドの互除法では O(d) 回の除算で最大公約数が求められる。桁数 d は O(log n) なので、ユークリッドの互除法では O(log n) 回の除算で最大公約数が求められる。

参考
- https://ja.wikipedia.org/wiki/%E3%83%A6%E3%83%BC%E3%82%AF%E3%83%AA%E3%83%83%E3%83%89%E3%81%AE%E4%BA%92%E9%99%A4%E6%B3%95#%E8%A8%88%E7%AE%97%E9%87%8F
  

- Typ022では計算郎がO(log(A+B))と紹介されている。簡単に見積もっているかだと思われる。正確にはO(log min(A, B))だと思われる。
- ３つの数におけるgcdの計算量は、O(log min(A, B, C))なのだろうか。gcd(gcd(A,B), C)のような実装すると、まずgcd(A,B)が実装されるので、O(log min(A, B, C))というよりはO(log(log min(A, B),C)なのではないだろうか。これも単純に簡単に見積もっているからだろうか。


## C++ の push_back
- 細かいことを言うと、push_back(値) が呼ばれたとき、既に確保したメモリに空きがない場合は、 メモリを再アロケート、データをコピー、以前のメモリを破棄、という処理が行われる。 これはデータ数が多い場合は結構重い処理なのだが、配列サイズが 0 から N になるまで push_back() を繰り返しても、 log N / log 2 回（または log N / log 1.5回）しか行われない。 なので厳密には O(1) ではないのだが、実質的には O(1) と理解しておいてよい。

## 効率の良い数値アレイ
- import array
- ex. a = array.array('i', [0,l])
- このモジュールでは、基本的な値 (文字、整数、浮動小数点数) のアレイ (array、配列) をコンパクトに表現できるオブジェクト型を定義しています。アレイはシーケンス (sequence) 型であり、中に入れるオブジェクトの型に制限があることを除けば、リストとまったく同じように振る舞います。オブジェクト生成時に一文字の 型コード を用いて型を指定します。
- abc 217 d
- https://docs.python.org/ja/3/library/array.html


## ２部グラフ
- グラフ理論における2部グラフ（にぶグラフ、英: bipartite graph）とは、頂点集合を2つに分割して各部分の頂点は互いに隣接しないようにできるグラフのことである。
- 辺で直接結ばれた頂点同士が互いに違う色となるように、頂点を２色で塗ることだできるグラフ。（四色定理：四色定理（よんしょくていり／ししょくていり、英: Four color theorem）とは、厳密ではないが日常的な直感で説明すると「平面上のいかなる地図も、隣接する領域が異なる色になるように塗り分けるには4色あれば十分だ」という定理である。）
- https://ja.wikipedia.org/wiki/2部グラフ
- https://github.com/E869120/kyopro_educational_90/blob/main/editorial/026.jpg
- https://hcpc-hokudai.github.io/archive/graph_max_matching_001.pdf

## in setが速い理由
- https://qiita.com/kitadakyou/items/6f877edd263f097e78f4


## 尺取り法
- 区間の左端と右端を尺取り虫のように動かすことで、条件を満たす区間を高速に見つける、というアルゴリズム

```
r=0, ans=0
for l = 0 to |S| - 1
    while S[l,r+1)をすべて 'X' に変えることが可能
        r = r + 1
    ans = max(ans, r - l)
```
- https://atcoder.jp/contests/abc229/editorial/2956


## 関数への参照渡し
- 関数内でも変数を代入するには、`global`を用いる必要がある。
- https://snowtree-injune.com/2018/07/29/post-738/Z
