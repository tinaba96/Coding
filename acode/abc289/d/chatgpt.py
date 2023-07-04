# 入力を受け取る
N = int(input())  # ロボットの動作回数
A = list(map(int, input().split()))  # ロボットが動作できる段数のリスト
M = int(input())  # モチの数
B = set(int(input()) for _ in range(M))  # モチがある段数の集合
X = int(input())  # 目的の段数

# DPテーブルを初期化する
dp = [False] * (X + 1)
dp[0] = True

# DPを実行する
for i in range(X + 1):
    if not dp[i]:
        continue
    for a in A:
        if i + a <= X and i + a not in B:
            dp[i + a] = True

# 結果を出力する
if dp[X]:
    print("Yes")
else:
    print("No")

'''
pythonで次の問題を解いてください。
無限に続く階段があります。 一番下は0 段目で、1 段のぼるごとに1 段目、2 段目と続きます。

0 段目に階段登りロボットがいます。 階段登りロボットは、一回の動作で
A1,A2,…,AN 段ぶん階段をのぼることができます。 つまり、階段登りロボットがi 段目にいるとき、一回動作をした後は
i+A1段目、
i+A2段目、⋯、
i+AN段目のいずれかにいることができます。 それ以外の段数を一回の動作でのぼることはできません。 階段登りロボットは階段を下ることもできません。

階段のB1,B2,…,BM段目にはモチが設置されています。 モチが設置されている段へのぼるとロボットは動けなくなり、他の段に移動することができなくなります。

階段登りロボットは階段のちょうどX 段目にのぼりたいです。 階段登りロボットが階段のちょうどX 段目にのぼることが可能か判定してください。
'''



'''
以下はPythonでの実装例です。

python
Copy code
# 入力を受け取る
N = int(input())  # ロボットの動作回数
A = list(map(int, input().split()))  # ロボットが動作できる段数のリスト
M = int(input())  # モチの数
B = set(int(input()) for _ in range(M))  # モチがある段数の集合
X = int(input())  # 目的の段数

# DPテーブルを初期化する
dp = [False] * (X + 1)
dp[0] = True

# DPを実行する
for i in range(X + 1):
    if not dp[i]:
        continue
    for a in A:
        if i + a <= X and i + a not in B:
            dp[i + a] = True

# 結果を出力する
if dp[X]:
    print("Yes")
else:
    print("No")
このコードでは、まず入力を受け取ります。次に、DPテーブルを初期化します。DPテーブルの要素 dp[i] は、ロボットが i 段目にいるときに、目的の段数 X に到達可能かどうかを表します。最初はロボットが 0 段目にいるので、dp[0] だけを True に設定します。

次に、DPを実行します。各 i について、dp[i] が True である場合、ロボットは i 段目にいることができます。ロボットが動作できる段数のリスト A を走査し、i + a 段目が X 以下であるかつモチのある段数の集合 B に属していない場合、ロボットは i + a 段目に移動できます。この場合、dp[i + a] を True に設定します。

最後に、dp[X] が True である場合、ロボットは X 段目に到達可能です。そうでない場合、ロボットは X 段目に到達できません。
'''
