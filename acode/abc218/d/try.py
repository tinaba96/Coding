import collections

from collections import defaultdict

ma = defaultdict(list)

N = int(input())
#ma = [[] for j in range(10**9)]
#p = {}
for i in range(N):
    x, y = list(map(int, input().split()))
    ma[x].append(y)
    #p[x] = y
cnt = 0
ans = []
#print(ma)
for i in range(len(ma)):
    for j in range(len(ma[i])):
        for k in range(i+1, len(ma)):
            if ma[i][j] in ma[k]: # this only see the y value
                ans.append((i,k)) # this is the pair of x values that have same value
                #print(i,k)

#print('ans', ans)
c = collections.Counter(ans)
#print('c', c)

an = 0
for i in c.keys():
    an += c[i]*(c[i]-1)//2
print(an)


# O(N^2) ?
# I think this will works in terms of time complexity but I don't know there are so many WA

'''
40
1 1
2 1
1 2
2 2
3 2
1 3
3 3
2 3
3 1
2 4
2 5
1 5
3 4
3 5
4 4
4 1
4 2
5 4
5 6
5 8
4 8
3 7
3 9
5 1
5 2
5 3
6 1
6 2
6 3
6 4
0 1
0 2
0 3
0 4
0 5
0 0
0 8
0 7
7 7
7 6
'''
#127




