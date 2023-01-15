import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N, M = list(map(int, input().split()))
mp = [[] for n in range(N+1)]
for i in range(M):
    u, v = list(map(int, input().split()))
    mp[u].append(v)
    mp[v].append(u)

al = set()
cnt = 0

def dfs(p, e):
    global cnt
    if p not in al:
        al.add(p)
    cnt += 1
    if len(al) > 10**6:
        print(10**6)
        exit()
    for n in mp[e]:
        if str(n) in p:
            continue
        dfs(p+str(n), n)
    return

dfs('1', 1)
print(cnt)

# WA: 全探索ができていない？
# TLE: len(al)やstr(n) in p に時間を要している？　それともpythonの再帰だから？ -> len(al) is O(1), str(n) in p is almopst O(NlogN) (this is the cause of TLE)
# len(al) can costs almost 10**6 specially at the end. -> this is wrong see below
# str(n) in p costs O(len(p)) which is O(N) at maximum -> almost O(NlogN)


'''
ask question in LINE

ME
ABC284Eなのですが、このように実装して提出した結果、AC: 21 WA: 9 TLE: 3というような結果になってしまいました。
TLEになる原因は、len(al)やstr(n) in p　だと思うのですが、WAになる原因が分かりません。パスを文字列として、setに格納していく実装なのですが、WAの原因分かる方いらっしゃいますでしょうか。

answer1
p = '1'+'2'のときに12も行ったことになるとか？
path graph (一直線のグラフ)だとalに入る文字数がO(n^2)になって大変なことになりませんか

ME
そうですね！確かにこれだと0-9までの頂点しか機能しないですね！
ありがとうございます！

ans2
dfs(p+‘$’+str(n), n)
とかってしたらこの問題は解決できそうですね

ME
al.add(p)のpの（文字列の）長さlen(p)がO(n^2)なるということでしょうか。(for ans1)
確かに頭に文字列をつければ、探索する際も特定できますね！ありがとうございます！(for ans2)

ans1
alに入っている文字列の合計の長さです

単純グラフなので、DFSする限りでは毎回必ず違ったpになるので、個数だけ管理しておけばよいです

ME
確かにそうなりますね！気づきませんでした、、
これは単純にメモリ制限的に引っかかるという考え方で良いのでしょうか。

勉強になります！

ans1
基本的にそのはず…賢い言語実装だとメモリ節約してくれるのもあった気がしますが

ME
ありがとうございます！

ちなみに、dfsの部分はO(N+M)だと思っているのですが、
それに加え、len(al)やstr(n) in p の部分がさらにO(N)かかり、全体的にO(N(N+M))ではないかと考えたのですが、考え方はあっているのでしょうか。
len(al)やstr(n) in pの部分はそれぞれalとpの長さの分計算コストかかると思っているのですが、それぞれの長さがNくらいになるのは最後の方だけだと思います。全体としてO(N(N+M)と考えて良いのでしょうか。

len(al)やstr(n) in pの部分は、ならし計算量でもO(1)にならないと思うので、ならし計算量でO(1)にならなければ、O(N)と考えれば良いのでしょうか？

asn3
(余計なお世話かもしれませんがnを文字列で表した時の長さはO(log n)なのでalに含まれる文字列の長さの合計にもlogが付くと思います)

ans4
len は定数時間じゃないですか？

ME
ありがとうございます！
これは、グラフの分岐があるためlogがつくということでしょうか。
一直線のグラフなどの最悪ケースでO(n^2)になるという理解で良いでしょうか？ (for ans3)

pythonは長さを別で用意していて、len()はO(1)のようでした。
ご指摘ありがとうございます！(for ans4)

ans3
nを文字列で表そうとすると、その桁数分の文字が必要で、その桁数というのがO(log n)なので文字列の長さ、つまり文字の個数の合計にlogが付くという話です
例えば1や3は1桁なので1文字で良いですが、100000は6桁なので6文字必要です

ans5
その問題、再帰関数を用いたdfsが一般的だと思うのですが、スタックを用いたdfs で実装するのは厳しそうですかね？

ME
そういうことですね！理解できました。ありがとうございます！(for ans3)

となると、TLEの原因はstr(n) in pの部分でpの長さ分コストがかかるという理解で良いのでしょうか。pは最大N回文字列が足され、それぞれ足される文字列の長さがO(logN)と考えるとpの長さは O (NlogN)という感じでしょうか。

実装まではしていないのですが、pythonの再帰処理が苦手であることを考えるとスタックによる実装の方が早くなるとは思います。
ただこれがTLEの原因なのでしょうか。それとも上記のstr(n) in pがボトルネックになっているのでしょうか。(for ans5)

ans3
正しいと思います
TLEの原因がこれで、もしTLが無限であった場合今度はalのメモリが原因でMLEになると思います

ans4
+str(n) も PyPy だと遅そうなのと、なんか "123" か 1 → 2 → 3 なのか 1 → 23 なのかの曖昧性があって壊れませんか？
後者が WA になってそうで、例えば
1 → 23 → 2 のときに、2 が踏めないと判断されそうです
あ、既に指摘されてましたごめんなさい

ME
ありがとうございます！非常に納得がいき、勉強になりました！(for ans3)

いえいえ！ありがとうございます！
具体例も非常に勉強になりました！(for ans4)

'''



