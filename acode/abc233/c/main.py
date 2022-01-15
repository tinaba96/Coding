N, X = list(map(int, input().split()))

mp = []

for i in range(N):
    A = list(map(int, input().split()))
    mp.append(A[1:])

#print(mp)

val = 1
d = 0
ans = []
# 復習で追加
ans_ans = 0

def cal(i, j, val, d, ans):
    # it should be global variables
    global ans_ans
    val *= mp[i][j]
    if i+1 == N:
        if val == X:
            ans.append(1)
            ans_ans += 1
            print(ans_ans)
        return
    for k in range(len(mp[i+1])):
        #print(ans)
        cal(i+1, k, val, d+1, ans)

for p in range(len(mp[0])):
    d = 0
    val = 1
    cal(0, p, val, d, ans)

#print(len(ans))
print(ans_ans)
#なぜansはintでは無理なのか
# 変数の場合はglobal変数にしないといけない
# 最定義を行った時点で、関数内で独立した変数として扱われるため
# chttps://snowtree-injune.com/2018/07/29/post-738/


