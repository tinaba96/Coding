S = str(input())

import collections

c = collections.Counter(S)



for i in c:
    if c[i] == 1:
        print(i)
        exit()

print(-1)

