S = str(input())
ss = []

for i in range(len(S)):
    ss.append(S[i])

import itertools

li = list(itertools.permutations(ss)) # this is heavy

sort = sorted(li)

print("".join(sort[0]))


