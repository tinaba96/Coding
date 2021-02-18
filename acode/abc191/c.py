H, W = list(map(int, input().split()))

S = [[0 for i in range(W)] for w in range(H)]
s = []

for h in range(H):
    #s = list(map(str, input().split()))
    s = str(input())
    for w in range(W):
        S[h][w] = s[w]

#print(S)

le = []
re = []
le2 = []
re2 = []

cnt = 0

flag = False

for h in range(H):
    for w in range(W):
        if S[h][w] == '#' and flag == False:
            if w in le2:
                cnt -= 1
            elif w not in le2 and h > 1:
                cnt += 1
            le.append(w)
            cnt += 1
            flag = True
        if S[h][w] == '.' and flag == True:
            #print('w',w)
            #print('re', re2)
            if w in re2:
                #print('yes')
                cnt -= 1
            elif w not in re2 and h > 1:
                cnt += 1
            re.append(w)
            cnt += 1
            flag = False
    if len(re) > 1:
        cnt += len(re)-1
    if len(le) > 1:
        cnt += len(le)-1
    le2 = le
    re2 = re
    re = []
    le = []

print(cnt+2)



