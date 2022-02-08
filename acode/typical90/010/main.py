N = int(input())
cum1 = [0]*N
cum2 = [0]*N
cls = [0]*N
c, p = list(map(int, input().split()))
if c == 1:
    cum1[0] = p
    cum2[0] = 0
else:
    cum1[0] = 0
    cum2[0] = p
cls[0] = c
for i in range(1, N):
    c, p = list(map(int, input().split()))
    if c == 1:
        cum1[i] = cum1[i-1] + p
        cum2[i] = cum2[i-1]
    else:
        cum1[i] = cum1[i-1] 
        cum2[i] = cum2[i-1] + p
    #cls[i] = c
#print('1', cum1)
#print('2', cum2)


Q = int(input())
for i in range(Q):
    l, r = list(map(int, input().split()))
    if l == 1:
        tmp1 = cum1[r-1]
        tmp2 = cum2[r-1]
    else:
        tmp1 = cum1[r-1] - cum1[l-2]
        tmp2 = cum2[r-1] - cum2[l-2]

    print(tmp1, tmp2)



