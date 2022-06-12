from collections import defaultdict
N, K = list(map(int, input().split()))
a = list(map(int, input().split()))

sort = sorted(a)

if K == 1:
    print('Yes')
    exit()

#}mp = [set() for p in range(K+1)]
'''
mp = []
for i in range(K+1):
    mp[i] = defaultdict(int)
'''
#mp = defaultdict(lambda :defaultdict(int))
mp = defaultdict(set)


for j in range(N):
    mp[j%K].add(a[j])

#print(mp)
#print(sort)
for i in range(N):
    if a[i] == sort[i]:
        continue
    else:
        ind = i%K
        if sort[i] not in mp[ind]:
        #if a[i] != sort[i+K]:
            print('No')
            exit()
print('Yes')


# i think this approach is logically correct.
# the only "No" answers is when the two numbers cannot swap.
# if there is a case that cannot swap due the the way we keep some values as set() but answer should be "Yes", those numbers should be same numbers that are not needed to be swapped

