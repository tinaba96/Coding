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
# if there are same number of vales or  more than K, it means it will not be "no" becuase of the set() (considered as one even if it has multiple
'''
K: 3
A: 5 1 5 5 8 5
sorted: 1 5 5 5 5 8 (-> "5" of index 4 can be realized anytime even if mp[] only has 1 because all the key in mp has at least one "5" and one of them must have 2 of "5")
-> moreover, there no case that only one key has multiple "5". if some key has multiple, it means all have at leasr one.
'''
# wait above comment is not important

# if mistakenly pass the condition because of set(), it will 100% fail on the other following number. because if the answer is "no":, there will be at least one pair that need to be replaced to be "yes". Thus even though one is mistakenly pass, the other will surely fail.


#therfore, there is no problem that we use set() instead of array.
