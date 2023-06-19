H,W =map(int,input().rstrip().split())
S = [list(input()) for _ in range(H)]

left, right = 1000, -1
top, bottom = 1000, -1

for h in range(H):
    for w in range(W):
        if S[h][w]=='#':
            left = min(left,w)
            right = max(right,w+1)
            top = min(top,h)
            bottom = max(bottom,h+1)
            
for h in range(top,bottom):
    for w in range(left,right):
        if S[h][w]=='.':
            print(h+1,w+1)
            break
