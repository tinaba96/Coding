#binary search

n = int(input())

def erastosthenes(n):
    data = [i for i in range(n + 1)]
    root = int(pow(n, 0.5))
    for i in range(2, root + 1):
        if data[i] != 0:
            for j in range(i, n + 1):
                if i * j >= n + 1:
                    break
                data[i*j] = 0
    primes = sorted(list(set(data)))[2:]
    return primes

def bin(x, A):
    left = 0
    right = len(A) - 1
    while left <= right:
        if A[(left + right) // 2] < x:
            left = (left + right) // 2 + 1
        else:
            right = (left + right) // 2 - 1
    return left

m = int(n ** (1/3) + 0.00001)
A = erastosthenes(m) #A ~ 10^6
ans = 0
if A is not None:
    for i in range(len(A)):
        num = int((n / A[i]) ** (1/3) + 0.00001)
        index = bin(num, A)
        if A[index] != num:
            index -= 1
        if index <= i:
            break
        ans += index - i
print(ans)
