import numpy as np
 
N = int(input())
A = list(map(int, input().split()))
 
# print(N, A)
called = np.zeros(N)
 
for i in range(N):
    if called[i] == 0:
        called[A[i]-1] = 1
 
uncalled = []
for i in range(N):
    if called[i] == 0:
        uncalled.append(str(i+1))
 
print(len(uncalled))
print(" ".join(uncalled))
