N = int(input())

rail = []
ans = [0 for i in range(10)]
mp = [0 for i in range(10)]
cnt = [0 for i in range(10)]

for i in range(N):
    S = str(input())
    rail.append(S)
 

for k in range(10):
    ch = set()
    t = 0
    last = 0
    for i in range(10):
        c = 0
        isV = False
        for j in range(N):
            if int(rail[j][i]) == k:
                isV = True
                if i in ch:
                    c += 1
                else:
                  ch.add(i)
        if isV == True:
            last = i
        if c >= t:
            t = c
            mp[k] = i
    
    print(10*t+mp[k], " ", last)
    ans[k] = max(10*t+mp[k], last)


print(ans)
print(min(ans))




