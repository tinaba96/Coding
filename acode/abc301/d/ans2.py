S = input()[::-1]  # reversed
N = int(input())

L = len(S)
Q = 0  # ? の個数
min_bit = 0  # ? を全て 0 にしたときの値
for i in range(L):
    min_bit |= (S[i] == '1') << i
    Q += S[i] == '?'


def sum_bit(m): # m is the all the cases when you choose Q as the number of "?"
    ans = min_bit
    q = 0
    for i in range(L):
        if S[i] == '?':
            ans |= (m >> q & 1) << i
            q += 1
    return ans


ok, ng = 0, 1 << Q  # [ok,ng)
while ng - ok > 1:
    m = (ok + ng) // 2
    if sum_bit(m) <= N:
        ok = m
    else:
        ng = m

ans = sum_bit(ok)
if ans > N:
    ans = -1
print(ans)


