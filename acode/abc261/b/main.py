N = int(input())

ans = 'correct'

mp = []

for i in range(N):
    A = list(map(str, input().split()))
    mp.append(A)

def comp(x, y):
    if x == 'W':
        if y == 'L':
            return True
        else:
            return False
    if x == 'L':
        if y == 'W':
            return True
        else:
            return False
    if x == '-':
        if y == '-':
            return True
        else:
            return False
    if x == 'D':
        if y == 'D':
            return True
        else:
            return False



#print(mp)
#print(mp[1][0][2])
for i in range(N):
    for j in range(N):
        if comp(mp[i][0][j], mp[j][0][i]) == False:
           # print(i,j)
            print('incorrect')
            exit()
print(ans)


