import math

def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

N = int(input())
tmp = N // 2 + 1
tmp = math.pow(tmp,1/3)
li = primes(int(tmp))

ans = 0
ans_test = set()
for q in li:
  for p in li:
    if p >= q:
      break
    if p*q**3 > N:
      break
    ans += 1
    ans_test.add(ans**2)
    #ans_test.add(p*q**3)


print(ans)

# Line open chat
'''
A いくらハッシュでも要素が多すぎると遅くなるようです。何故かはよくわかってないです。(衝突するから？)
B 衝突が一番あり得そうです
いや、衝突ではなくて、単に定数倍遅いだけな気がします
ans.add(100)は最初の一回以外は何もしないので速いです
ME ありがとうございます！
検証すると、確かに要素が多いと時間がかかるようですね。
衝突して遅くなるのは納得が行きます！
単に定数倍遅いというのはどういうことでしょうか。
そうでした、、失礼しました。
B ans+=1とans.add(整数)は、同じO(1)時間でもかかる時間が後者の方が長いです。これは、足し算にくらべてaddの方が複雑な処理(ハッシュ値の計算・メモリアクセス・衝突した場合は次の要素を探す・ハッシュテーブルの大きさが足りない場合は伸長)をしているためです
このことを俗に「定数倍遅い」と言ったりします
ME なるほどですね！
非常に勉強になります！ありがとうございます！
正確にいうと衝突によってTLEしたというよりは、
set()の方が、複雑な処理によって定数倍遅いから（そのような余分な処理が積み重なって）TLEした
の方が認識として正しいということでしょうか。

'''

