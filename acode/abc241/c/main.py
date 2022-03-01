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


# reverse
for i in range(N):
    o = 0
    x = 0
    righttop = N-1
    leftbottom = N-6
    for j in range(6):
        if i+j >= i+6:
            break
        if mp[j][N-1-i-j] == '#':
            x += 1
        else:
            o += 1

    if o <= 2 and (o+x >= 6):
        print('Yes')
        exit()
        
    for j in range(N-6):
        if i+righttop < 0 or i+righttop >= N:
            break
        #print('bef', N-righttop-1, i+righttop)
        if mp[N-righttop-1][i+righttop] == '#':
            x -= 1
        else:
            o -= 1
        righttop -= 1

        if o <= 2 and (o+x >= 6):
            print('Yes')
            exit()

        leftbottom -= 1
        if i+leftbottom < 0 or i+leftbottom >= N:
            break
        if mp[N-leftbottom-1][leftbottom+i] == '#':
            x += 1
        else:
            o += 1

        if o <= 2 and (o+x >= 6):
            print('Yes')
            exit()

for i in range(N):
    o = 0
    x = 0
    righttop = N-1
    leftbottom = N-6
   # if i == 2 or i == 3:
        #print('-------')
    for j in range(6):
        if N-1-i-j < 0:
            break
        #print('first', i+j, N-1-j)
        if mp[i+j][N-1-j] == '#':
            x += 1
        else:
            o += 1

    if o <= 2 and (o+x >= 6):
        print('Yes')
        exit()
        
    for j in range(N-6):
        if N-righttop-1+i < 0 or N-righttop-1+i >= N:
            break
        #print('bef', N-righttop-1+i, righttop)
        if mp[N-righttop-1+i][righttop] == '#':
            x -= 1
        else:
            o -= 1
        righttop -= 1

        if o <= 2 and (o+x >= 6):
            print('Yes')
            exit()

        leftbottom -= 1
        if N-leftbottom-1+i < 0 or N-leftbottom-1+i >= N:
            break
        #print('aft', N-lefttop-1+i, lefttop)
        if mp[N-leftbottom-1+i][leftbottom] == '#':
            x += 1
        else:
            o += 1

        if o <= 2 and (o+x >= 6):
            print('Yes')
            exit()
print('No')

# there are still some WA, it is still weird
'''
8
........
........
........
......#.
.....#..
........
...#....
..#.....


10
..........
..........
.........#
..........
..........
......#...
..........
....#.....
...#......
..#.......
Yes
'''
