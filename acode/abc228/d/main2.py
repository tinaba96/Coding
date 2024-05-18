from collections import defaultdict

Q = int(input())

N = 2 **20
A = defaultdict(lambda: -1) # I think this takes time because it will create a new key in the loop (length also need to be calculated in each time)
# if it is defined as array, it will not be TLE
# it is time consuming to create each keys as the default value of -1 than creating an array whose length is N
# A = [-1] * N 
# but I think this will not make the big difference 
mp = [0 for i in range(N+1)]

for q in range(Q):
    t, x = list(map(int, input().split()))
    if t == 1:
        h = x
        while A[h%N] != -1:
            h += mp[h%N] + 1
        A[h%N] = x
        mp[x%N] = h-x
    else:
        print(A[x%N])
    
# In conclusion, the reason why there was an TLE is because the Order is different with the answer.
# I think what it became AC by changing it to Array is just a coincident.
# this approach does not reduce the time when there is so many small changes (it will move to next index one by one so many times in order to get the final root while the answer use the last root as the next index by using root()) as also mentioned in the video editoral.



