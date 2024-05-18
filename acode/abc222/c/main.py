import copy
N, M = list(map(int, input().split()))

mp = []
numWins = [0 for i in range(2*N)]
   
for i in range(2*N):
    A = list(map(str, input().split()))
    mp.append(A)

order = [i for i in range(2*N)]
#print('ord', order)
def ord(numWins):
    de = sorted(numWins, reverse=True)
    tmp =[] 
#print('de',de)
    tmpWins = copy.copy(numWins)
    for e in de:
        if e in tmpWins:
            index = tmpWins.index(e)
            tmpWins[index] = -1
            tmp.append(index)
    return tmp
    #print(numWins)

for m in range(M): #ROund
    win = []
    draw = []
    lose = []
    for n in range(0, 2*N, 2):
        #print(n)
        #print('vs', order[n], ':', order[n+1])
        if (mp[order[n]][0][m] == 'P' and mp[order[n+1]][0][m] == 'C') or (mp[order[n]][0][m] == 'C' and mp[order[n+1]][0][m] == 'G') or (mp[order[n]][0][m] == 'G' and mp[order[n+1]][0][m] == 'P'):
            #print('m :', m, 'n : ', n)
            win.append(order[n+1])
            numWins[order[n+1]] += 1
            lose.append(order[n])
        elif (mp[order[n]][0][m] == 'G' and mp[order[n+1]][0][m] == 'C') or (mp[order[n]][0][m] == 'P' and mp[order[n+1]][0][m] == 'G') or (mp[order[n]][0][m] == 'C' and mp[order[n+1]][0][m] == 'P'):
            win.append(order[n])
            numWins[order[n]] += 1
            lose.append(order[n+1])
        else:
            draw.append(order[n])
            draw.append(order[n+1])

    order = win + draw + lose
    order = ord(numWins)



de = sorted(numWins, reverse=True)
ans =[] 
#print('de',de)
for e in de:
    if e in numWins:
        index = numWins.index(e)
        numWins[index] = -1
        ans.append(index)


#print(mp)
for e in ans:
    print(e+1)
#print(mp[1][0][1])

