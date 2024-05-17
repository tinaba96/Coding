from collections import defaultdict
mp = defaultdict(int)

N = int(input())
for i in range(N):
    S = str(input())
    mp[S] += 1

#print(mp)
print(max(mp, key=mp.get))


