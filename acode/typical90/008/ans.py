from collections import defaultdict
MOD = 10**9 + 7
N = int(input())
S = input()
C = defaultdict(int)
ATCODER = 'atcoder'
dp = [0] * (len(ATCODER)+1)
for s in S:
    if s in ATCODER:
        i = ATCODER.index(s)
        if i == 0:
            dp[0] += 1
        if 0 < i :
            #dp[i+1] += dp[i] % MOD
        #dp[i] += dp[i] % MOD
            dp[i] = (dp[i]+dp[i-1]) % MOD
        #print(dp)
print(dp[6]%MOD)

