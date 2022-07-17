H, W = list(map(int, input().split()))

mp = [['.' for i in range(W) ] for j in range(H)]

mp[0][0] = '#'

for w in range(W):
    for h in range(H):
        if mp[h][w] == '#':
            mp[h+1][w] = '.'
            mp[h][w+1] = '.'
            mp[h+1][w+1] = '.'
        else:




#print(mp)



