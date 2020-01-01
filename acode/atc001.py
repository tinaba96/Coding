from numpy.fft import rfft, irfft

N, *AB = map(int, open(0).read().split())
A, B = AB[::2], AB[1::2]

M = 2 * 10 ** 5
X = irfft(rfft(A, M) * rfft(B, M))

print(0)
print(*map(int, X[:2 * N - 1] + 0.5), sep='\n')

