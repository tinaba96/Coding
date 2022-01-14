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
ans_ans

def cal(i, j, val, d, ans, ans_ans):
    val *= mp[i][j]
    if i+1 == N:
        if val == X:
            ans.append(1)
            ans_ans += 1
        #print(val)
        return
    for k in range(len(mp[i+1])):
        #print(ans)
        cal(i+1, k, val, d+1, ans)

for p in range(len(mp[0])):
    d = 0
    val = 1
    cal(0, p, val, d, ans)

print(len(ans))
#なぜansはintでは無理なのか


