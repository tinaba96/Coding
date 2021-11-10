H, W = list(map(int, input().split()))

ma = [[] for i in range(H)]

for h in range(H):
    A = list(map(int, input().split()))
    ma[h] = A


for hi in range(H):
    for hj in range(hi, H):
        for wi in range(W):
            for wj in range(wi, W):
                if ma[hi][wi] + ma[hj][wj] > ma[hj][wi] + ma[hi][wj]:
                    print('No')
                    exit()
print('Yes')

        





