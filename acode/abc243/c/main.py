N = int(input())

xarr = []
yarr = []

for i in range(N):
    x, y = list(map(int, input().split()))
    xarr.append(x)
    yarr.append(y)



S = str(input())

from collections import defaultdict
dic = defaultdict(lambda: -1)

for i in range(len(S)):
    if S[i] == 'R':
        if dic[yarr[i]] == -1:
            dic[yarr[i]] = xarr[i]
        else:
            if dic[yarr[i]] > xarr[i]:
                dic[yarr[i]] = xarr[i]

for i in range(len(S)):
    if S[i] == 'L':
        if dic[yarr[i]] != -1 and dic[yarr[i]] < xarr[i]:
            print('Yes')
            exit()
print('No')



