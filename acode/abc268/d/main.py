import itertools
import collections


N, M = list(map(int, input().split()))

ss = []

check = set()
cnt = 0

for i in range(N):
    S = str(input())
    ss.append(S)
    cnt += len(S)

for k in range(M):
    T = str(input())
    check.add(T)


mar = 16-cnt-N+1

for v in itertools.permutations(ss, N):
    z = '_'
    if len(z.join(v)) > 16 or len(z.join(v)) < 3:
        print('-1')
        exit()

    if len(z.join(v)) <= 16 and z.join(v) not in check:
        print(z.join(v))
        exit()

    comb = []
    for com in range(N-1):
        comb.append(str(com))
    comb.append('-1')

    for vc in itertools.combinations_with_replacement(comb, mar):
        #print(vc)
        counter = collections.Counter(vc)
        #print(counter)
        co = ''
        for i in range(N):
            co += v[i]
            if i == N-1:
                break
            co += '_'
            for h in range(counter[str(i)]):
                co += '_'
        if co not in check:
            print(co)
            exit()


print('-1')
