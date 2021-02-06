H, W = list(map(int, input().split()))

S = [[0 for i in range(W)] for w in range(H)]
s = []

for h in range(H):
    #s = list(map(str, input().split()))
    s = str(input())
    for w in range(W):
        S[h][w] = s[w]

cnt = 0
for h in range(1,H-1):
    for w in range(1,W-1):
        if S[h][w] == '#':
            cnt += 1
            if S[h-1][w] == '#' and S[h+1][w] == '#' or S[h][w-1] == '#' and S[h][w+1] == '#':
                cnt -= 1
        if S[h][w] == '.':
            if S[h-1][w] == '#' and S[h+1][w] == '#' or S[h][w-1] == '#' and S[h][w+1] == '#':
                cnt += 1
          


print(cnt)



