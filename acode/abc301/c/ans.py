from collections import Counter

S = input()
T = input()

S_cnt = Counter(S)
T_cnt = Counter(T)

A = 'atcoder'
al = 'abcdefghijklmnopqrstuvwxyz'
N = len(al)
for i in range(N):
    x = al[i]

    if S_cnt[x] == T_cnt[x]: continue

    if x not in A: exit(print('No'))

    if S_cnt[x] < T_cnt[x]:
        S_cnt['@'] -= T_cnt[x] - S_cnt[x]
    elif S_cnt[x] > T_cnt[x]:
        T_cnt['@'] -= S_cnt[x] - T_cnt[x]

#if S_cnt['@'] >= 0 and T_cnt['@'] >= 0 and S_cnt['@'] == T_cnt['@']:
if S_cnt['@'] >= 0: # this is enough (my idea)
    print('Yes')
else:
    print('No')


