import collections

cnter = collections.Counter


S = str(input())
ans = 0

cc = cnter(S)

print(cc['c']*cc['h']*cc['o']*cc['k']*cc['u']*cc['d']*cc['a']*cc['i'])

for i in range(len(S)):
    if S[i] == 'c':
        for c in range(i, len(S)):
            if S[c] == 'h':
                for h in range(c, len(S)):
                    if S[h] == 'o':
                        for o in range(h, len(S)):
                            if S[o] == 'k':
                                for k in range(o, len(S)):
                                    if S[k] == 'u':
                                        for u in range(k, len(S)):
                                            if S[u] == 'd':
                                                for d in range(u, len(S)):
                                                    if S[d] == 'a':
                                                        for a in range(d, len(S)):
                                                            if S[a] == 'i':
                                                                ans += 1

        

print(ans)


tot = 1
key = ['c','h','o','k','u','d','a','i']


def func(index, k):
    for i in range(index, len(S)):
        if S[i] == key[k]:
            func(i, key[k+1])



    
