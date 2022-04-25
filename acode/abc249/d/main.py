import collections

N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)

s = set(A)

mp = list(s)

mp.sort()

ans = 0

for i in range(len(mp)):
    for j in range(i+1, len(mp)): # no need to check this much. M/i is enough which leads to AC
        if mp[i]*mp[j] in s:
            #print('i', i, ':', mp[i])
            #print('j', j, ':', mp[j])
            ans += c[mp[i]]*c[mp[j]]*c[mp[i]*mp[j]]*2


for i in range(len(mp)):
    if mp[i]**2 in s:
        ans += c[mp[i]]*c[mp[i]]*c[mp[i]*mp[i]]


print(ans)

