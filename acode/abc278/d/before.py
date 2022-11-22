import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N = int(input())
A = list(map(int, input().split()))
Q = int(input())

mp = []
st = []

for i in range(Q):
    q = list(map(int, input().split()))
    mp.append(q)
    if q[0] == 3:
        st.append(i)

ans = []
#print('st: ', st)

for s in range(len(st)-1, -1, -1):
    target = mp[st[s]][1]
    ind = st[s] - 1
    an = A[target-1]
    while True:
        if ind < 0:
            ans.append(an)
            #ans.append(A[target-1])
            break
        if mp[ind][0] == 1:
            an += mp[ind][1]
            an -= A[target-1]
            ans.append(an)
            break

        if mp[ind][0] == 2 and mp[ind][1] == target:
            an += mp[ind][2]
        ind -= 1

#print(mp)

#print(ans)

for k in range(len(ans)):
    print(ans[-1-k])


