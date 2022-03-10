import sys
sys.setrecursionlimit(10000000)
N = int(input())
mp = [[-1 for i in range(10)] for j in range(N+1)]
# 残りrで最後がdのとき、残りの埋め方
def memo(r, d):
    if r == 1:
        mp[r][d] = 1
        return 1
    if mp[r][d] != -1:
        return mp[r][d]
    val = 0
    if 1<d<9:
        val += memo(r-1, d-1)
        val += memo(r-1, d)
        val += memo(r-1, d+1)
    elif d == 1:
        val += memo(r-1, d)
        val += memo(r-1, d+1)
    elif d == 9:
        val += memo(r-1, d-1)
        val += memo(r-1, d)
    mp[r][d] = val%998244353
    return val%998244353
ans = 0
for i in range(1, 10):
    ans += memo(N, i)
print(ans%998244353)

'''
i asked the LINE openchat

A: 色々試してみたんですが、再帰だとPythonで解くのは難しそうです C++で同じのを実装したのですが、10^6で200msでした

B:これ確かにO(N)なんですけど、厳密にはO(30*N)ですよね？普通は定数倍のところは無視しますけど、この問題だと定数倍が結構でかくて最大ケースだと10の7乗の計算量になりますよね。
DPだとPypyだと通るけどPythonだとTLEしますので、計算量的にはPypyじゃないと厳しいです。ただ、Python→リストへのアクセスが遅い、Pypy→再帰が遅いので、メモ化再帰だとどっちかを選ぶともう片方が遅くなってTLEしちゃうんだと思います。あくまで1考察です。

B: 上の方のアドバイスも加味すると、方針と計算量は問題ないのですが言語のせいみたいですね😭

A: そうですね... 自分は出来るだけ再帰を使わない方針で考えて、どうしても使わないといけない時はC++で解くようにしてます

B: 結論:男は黙ってC++💪(`･ω･´💪)(なお、ワイもPython使いの模様)

'''

