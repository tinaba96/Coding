'''
from numpy.fft import rfft, irfft

N, *AB = map(int, open(0).read().split())
A, B = AB[::2], AB[1::2]

M = 2 * 10 ** 5
X = irfft(rfft(A, M) * rfft(B, M))

print(0)
print(*map(int, X[:2 * N - 1] + 0.5), sep='\n')

'''

import numpy as np

N = int(input())
n0 = 2**int(np.ceil(np.log2(2*N - 1)))

A = np.zeros(n0)
B = np.zeros(n0)
for i in range(N):
    A[i], B[i] = map(int, input().split())
print('A:',A)
print('B:',B)
C = np.fft.ifft( np.fft.fft(A)*np.fft.fft(B) )
print(C)
print(0)
for ci in np.real(C[:2*N - 1] + 0.5):
    print(int(ci))

