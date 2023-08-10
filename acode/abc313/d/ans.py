# QA
def qa(q:list):
    # 問い合わせ
    print(*(['?']+q))
    # 偶奇の回答
    return int(input())

n, k = map(int, input().split())
base=[]
# 1~K+1の範囲を1個ずつずらしながら偶奇を判定
for i in range(k+1):
    q=[j%(k+1)+1 for j in range(i,i+k)]
    base.append(qa(q))
ans=[0]*(k+1)
# 1~K+1の偶奇
sm=sum(base)%2 # Kが奇数だからこの値は全体の合計を意味する
# K+1個とK個の差でSiの偶奇を求める
for i in range(k+1):
    ans[(k+i)%(k+1)]=sm^base[i]
# 確定した1~K-1を使ってK+2以降を判定するため後ろ2個を除外
sm^=ans[-2]^ans[-1]
# 確定した1~K-1の位置番号作成
base=[i for i in range(1,k)]
# 確定した1~K-1と未確定のK+iのK個で偶奇を判定
for i in range(k+1,n):
    ans.append(qa(base+[i+1])^sm)
# 答え
print(*(['!']+ans))
