N, M = list(map(int, input().split()))

import itertools

l = []

for i in range(M):
    l.append(str(i+1))

#if N == 1:



m = []
for v in itertools.combinations(l, N):
    #print(sorted(list(v)))
    m.append(int(''.join(v)))
    #print(*v)
ans = sorted(m)
print(m)
print(ans)
#print(ans)


# misunderstanding
# Since i separate 10 to 1 and 0, and i delete the last digit which is 0 (actually part of 10),
# i though the digit is not in order because 1 is placed at last. 
# However, it is part of 10 and, itertools already make it in order. So I should not have done anything with it. もったいない

