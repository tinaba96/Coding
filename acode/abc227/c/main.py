import math

N = int(input())

lim = 10 **11
cnt = 0
test = [1, 2, 3, 4, 5]

root = N**(1/3)

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)
print(root)
t = permutations_count(int(root)+1, 3)
print(t)

'''
for i in range(1, N+1):
    for j in range(i, N+1):
        for k in range(j, N+1):
            #print(i,j,k)
            if i*j*k <= N:
                cnt += 1
'''

