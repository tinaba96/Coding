N = int(input())
S = str(input())
Q = int(input())

mp = {}

for s in range(len(S)):
    mp[str(s)] = s

# print(mp)
arr = [[0 for i in range(2)] for j in range(Q*2*N)]

ex = -1
for q in range(Q):
    t, a, b = list(map(int, input().split()))
    if (t==1):
        if (a >= b):
            arr[q + ex] = [b, a]
        else:
            arr[q + ex] = [a, b]
    else:
        for i in range(N):
            ex += 1 
            arr[q + ex] = [i, N+i]
    


print(arr)



'''
    if ( t == 1):
        (mp[str(a-1)],mp[str(b-1)]) = (mp[str(b-1)],mp[str(a-1)])


    else:
        for i in range(N):
            (mp[str(i)],mp[str(N+i)]) = (mp[str(N+i)],mp[str(i)])
'''


    # print(S)
for k, v in mp.items():
    print (k, v)
    # s[k] = v

print(S)




