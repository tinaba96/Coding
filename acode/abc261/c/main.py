from collections import defaultdict
d = defaultdict(int)

N = int(input())

h = set()

for i in range(N):
    S = str(input())
    if S not in h:
        h.add(S)
        print(S)
    else:
        d[S] += 1
        print(S + '(' + str(d[S]) + ')')


#print(d)





