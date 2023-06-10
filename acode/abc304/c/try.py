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


N, D = list(map(int, input().split()))

all = []

for i in range(N):
    x, y = list(map(int, input().split()))
    all.append((x, y))

import math

mp = [[] for _ in range(N)]

for i in range(N):
    for j in range(i,N):
        a1 = all[i][0]
        a2 = all[i][1]
        b1 = all[j][0]
        b2 = all[j][1]
        #d = abs(a1-b1)**2 + abs(a2-b2)**2
        d = math.sqrt(abs(a1-b1)**2 + abs(a2-b2)**2)

        if d <= D:
            mp[i].append(j)
            mp[j].append(i)


#print(mp)
ans = [False for f in range(N)]

q = [0]

while q:
    v = q.pop()
    for g in range(len(mp[v])):

        nx = mp[v][g]
        if ans[nx] == True:
            continue
        else:
            #ans[nx] = True # this is AC
            q.append(nx)
    ans[v] = True  # this was the cause of TLE -> same value can be in the que so many times (maximum O(N^3)?) => see below


#print(ans)

for a in ans:
    if a == True:
        print('Yes')
    else:
        print('No')

'''
LINE openchat
お忙しい中申し訳ありません、abc304Cに関連してもう一つ質問させて下さい。計算量の見積もり方についてです。
下記のソースコードは、while文の中のans[v]=Trueの位置によってTLEするコードです。このTrue処理をwhile文の中にあるfor文の中に入れるとACします。（これは同じ頂点をキューに入れにくくなるからです。）



そこで、このTLEになるソースコードの計算量を見積もりたいと思って考えているのですが、O (N^3)なのかもっと大きいのかよく分かりません。
最悪ケースを考えようとしてもうまく見積もることができません。見積もり方も含めて教えて頂けないでしょうか。

この実装は、連結した頂点（感染する人）をキューに全て入れた後のみ、元の頂点をTrueにする（非効率な）形になっています。
また、キューから取り出した際に、すでにTrueになっているかの判定をしないため、同じ頂点がキューにある場合は、連結した頂点がその分何回もキューに挿入されることになります。
唯一キューに挿入される頂点が減っていくケースは、連結した頂点を挿入していく段階で、Trueになっている頂点に遭遇する場合です。（実際に処理が遅くなるのは、結構稀なケースにはなると思います。実際に提出してTLEしたテストケースは2個のみ（残りはAC）でした。）
非常に効率の悪い実装なのですが、計算量の見積もりの仕方を知りたく思っています。

宜しくお願いします。




ありがとうございます。以下が自分なりに考えた考察になります。

(1) 全ての頂点が連結する場合は、最初の頂点が処理された時点で、全ての頂点(N)がキューに入り、順に取り出され実行されます。そして、その一つ一つも、連結する全頂点（N)をキューに挿入することになるので、O(N^2)くらいかと思います。

(2) ただ最悪ケースは、最初の頂点から連結している（辺が存在している）のが、N/2個あり、それらが残りのN/2個に連結している（辺が存在している）場合だと思いました。
この場合、最初の頂点の処理で、N/2個キューに挿入され、それらそれぞれが残りのN/2個を挿入するのでO(N^2)くらいになるかと思います。

(3) ただ、上記と同じような要領で、最初にN/3個挿入され、その後に(2)の処理がされると、O(N^3)になるのかと考えました。

このように（結構雑に）考えると、オーダーがどんどん増えていってしまいます。（分母も増えていくので、いずれオーダーは減っていくと思いますが）
ただ普通に考えると、処理が進むに連れて、すでに処理済みの頂点が増え、挿入される頂点は少しづづ減っていくと思うので、計算量をうまく見積れません。
そもそも上記が最悪ケースなのかも正直不安です、、ご意見いただけますでしょうか。






reply
while ループが何回繰り返されるか（=キューに頂点が追加される回数が何回か）を考えてみる。すべての頂点間に辺がある場合どうか。

-> No specific Reply

'''

