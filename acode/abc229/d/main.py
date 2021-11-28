S = str(input())
K = int(input())

before = 0
after = 0
between = 0

comp = 0

mp = []

isx = True
val = 0

lenS = len(S)

#S += 'aaaaa'
#print(S)

for i in range(len(S)):
    if S[i] == '.':
        if isx == False:
            between += 1
        else:
            if between != 0:
                mp.append((between, before+after))
            between = 1
        isx = False
    else:
        if isx == True:
            after += 1
        else:
            before = after
            after = 1
        isx = True

if S[-1] == 'X':
    mp.append((between, before+after))
else:
    mp.append((between, after))


mp = sorted(mp, reverse = True)
#print(mp)

ans = 0

for i in range(len(mp)):
    if K >= mp[i][0]:
        #print(mp[i][0])
        ans += mp[i][0] + mp[i][1]
        K -= mp[i][0]

print(ans)



