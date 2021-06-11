n=int(input())
t=list(map(int,input().split()))
dp=1
for x in t:dp|=dp<<x
dp=bin(dp)
ans=10**18
tot=sum(t)
for i in range(tot+1):
  if dp[-i-1]=="1":ans=min(ans,max(i,tot-i))
print(ans)



#another ans
def main():
    N = int(input())
    T = list(map(int, input().split()))

    # あらかじめ合計時間を出しておく。
    total = sum(T)

    # 公式解説では DP を用意して行っているが、
    # ここでは set を用いて、あり得る部分和を管理する。
    sums = set([0])
    for t in T:

        # 今回追加される部分和
        addition = set()

        for s in sums:
            # 総和の半分以下のものだけ使用する。
            if s + t <= total // 2:
                addition.add(s + t)

        # 前回の部分和の集合に、今回作成した集合を加える
        sums = sums | addition

    # 総和から部分和のうち最大のものを引いたのが答え
    result = total - max(sums)

    print(result)

main()


