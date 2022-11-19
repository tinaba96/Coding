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

if len(st) > 10**4:
    for g in mp:
        if g[0] == 1:
            for ks in st:
                A[mp[ks][1]-1] = g[1]
        if g[0] == 2:
            A[g[1]-1] += g[2]
        if g[0] == 3:
            print(A[g[1]-1])


else:








    ans = []
#print('st: ', st)
    val = -1

    for s in range(len(st)):
        target = mp[st[s]][1]
        ind = st[s] - 1
        if val == -1:
            an = A[target-1]
        else:
            an = val

        while True:
            if ind < 0:
                ans.append(an)
                #ans.append(A[target-1])
                break
            if mp[ind][0] == 1:
                an += mp[ind][1]
                if val == -1:
                    an -= A[target-1]
                else:
                    an -= val
                ans.append(an)
                val = mp[ind][1]
                break

            if mp[ind][0] == 2 and mp[ind][1] == target:
                an += mp[ind][2]

            #if mp[ind][0] == 3:



            ind -= 1

#print(mp)

#print(ans)

    for k in range(len(ans)):
        #print(ans[-1-k])
        print(ans[k])


