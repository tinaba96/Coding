N = int(input())
mp = []
for i in range(N):
    S = list(str(input()))
    o = 0
    x = 0
    for j in range(6):
        if S[j] == '#':
            x += 1
        else:
            o += 1
    left = 0
    right = 5
    if o <= 2 and (o+x >= 6):
        print('Yes')
        exit()
    for j in range(N-6):
        if S[left] == '#':
            x -= 1
        else:
            o -= 1
        left += 1

        if o <= 2 and (o+x >= 6):
            print('Yes')
            exit()

        right += 1
        if S[right] == '#':
            x += 1
        else:
            o += 1

        if o <= 2 and (o+x >= 6):
            print('Yes')
            exit()
    mp.append(S)

o = 0
x = 0
for i in range(N):
    top = 0
    bottom = 5
    for j in range(6):
        if mp[j][i] == '#':
            x += 1
        else:
            o += 1

    if o <= 2 and (o+x >= 6):
        print('Yes')
        exit()
        

    for j in range(N-6):
        if mp[top][i] == '#':
            x -= 1
        else:
            o -= 1
        top += 1

        if o <= 2 and (o+x >= 6):
            print('Yes')
            exit()

        bottom += 1
        if mp[bottom][i] == '#':
            x += 1
        else:
            o += 1

        if o <= 2 and (o+x >= 6):
            print('Yes')
            exit()




# go right
for i in range(N):
    o = 0
    x = 0
    lefttop = 0
    rightbottom = 5
    for j in range(6):
        if i+j >= i+6 or i+6 >= N:
            break
        if mp[j][i+j] == '#':
            x += 1
        else:
            o += 1

    if o <= 2 and (o+x >= 6):
        print('Yes')
        exit()
        
    for j in range(N-6):
        if i+lefttop >= N:
            break
        if mp[lefttop][i+lefttop] == '#':
            x -= 1
        else:
            o -= 1
        lefttop += 1

        if o <= 2 and (o+x >= 6):
            print('Yes')
            exit()

        rightbottom += 1
        if i+rightbottom >= N:
            break
        if mp[rightbottom][rightbottom+i] == '#':
            x += 1
        else:
            o += 1

        if o <= 2 and (o+x >= 6):
            print('Yes')
            exit()

#go bottom
for j in range(N):
    o = 0
    x = 0
    lefttop = 0
    rightbottom = 5
    for i in range(6):
        if i+j >= j+6 or j+6 >= N:
            break
        if mp[j+i][i] == '#':
            x += 1
        else:
            o += 1

    if o <= 2 and (o+x >= 6):
        print('Yes')
        exit()
        
    for i in range(N-6):
        if j+lefttop >= N:
            break
        if mp[j+lefttop][lefttop] == '#':
            x -= 1
        else:
            o -= 1
        lefttop += 1

        if o <= 2 and (o+x >= 6):
            print('Yes')
            exit()

        rightbottom += 1
        if j+rightbottom >= N:
            break
        if mp[j+rightbottom][rightbottom] == '#':
            x += 1
        else:
            o += 1

        if o <= 2 and (o+x >= 6):
            print('Yes')
            exit()

print('No')

'''
# reverse
for i in range(N):
    o = 0
    x = 0
    lefttop = 0
    rightbottom = 5
    for j in range(0, 6, -1):
        if i+j >= i+6:
            break
        if mp[j][i+j] == '#':
            x += 1
        else:
            o += 1

    if o <= 2 and (o+x >= 6):
        print('Yes')
        exit()
        
    for j in range(0, N-6, -1):
        if i+lefttop >= N:
            break
        if mp[lefttop][i+lefttop] == '#':
            x -= 1
        else:
            o -= 1
        lefttop += 1

        if o <= 2 and (o+x >= 6):
            print('Yes')
            exit()

        rightbottom += 1
        if i+rightbottom >= N:
            break
        if mp[rightbottom][rightbottom+i] == '#':
            x += 1
        else:
            o += 1

        if o <= 2 and (o+x >= 6):
            print('Yes')
            exit()

'''
