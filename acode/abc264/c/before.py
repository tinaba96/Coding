A = []
B = []

ch = []

H, W = list(map(int, input().split()))

for i in range(H):
    I = list(map(int, input().split()))
    A.append(I)

check = []

H2, W2 = list(map(int, input().split()))
for j in range(H2):
    J = list(map(int, input().split()))
    ch.append((i, J[0]))
    B.append(J)



if H < H2 or W < W2:
    print('No')
    exit()

#for k in range(len(ch)):

flag = []
#c = ch[k][1]
index = 0
cols = []
for h in range(H):
    cnt = 0
    flagC = False
    for w in range(W):
        c = B[index][cnt]
        if c == A[h][w]:
            flagC = True
            index += 1
            flagR = False
            for p in range(h, H):
                if B[index][cnt] == A[p][w]:
                    flagR = True
                    index += 1
                    if index == H2:
                        break
            if flagR == False:
                print('No')
                exit()

            cnt += 1
            if cnt == W2 or index == H2:
                print('Yes')
                exit()

        if flagC == False:
            print('No')
            exit()

print('Yes')




