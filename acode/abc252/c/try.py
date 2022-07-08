N = int(input())

rail = []
ans = [0 for i in range(10)]
mp = [0 for i in range(10)]
cnt = [0 for i in range(10)]

for i in range(N):
    S = str(input())
    rail.append(S)
 

for k in range(10):
    #t = 0
    #last = 0
    m = 0
    for i in range(10):
        c = -1
        #isV = False
        for j in range(N):
            if int(rail[j][i]) == k:
                #isV = True
                c += 1
        m = max(m, i+10*c) 
        '''
        if isV == True:
            last = i
        if c >= t:
            t = c
            mp[k] = i
        '''
    
    #print(mp[k], " ", last)
    #ans[k] = max(10*t+mp[k], last)
    ans[k] = m


#print(ans)
print(min(ans))




