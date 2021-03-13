
A, B, W = list(map(int, input().split()))


cnt = 0
cnt2 = 0


for i in range(1,1001):
    tmp = 1000*W-B*i
    if tmp==0:
        print(i)
    for j in range(1, 1000):
        for k in range(B-A):
            if (B-k)*j==tmp:
                print(i+j)
                break





