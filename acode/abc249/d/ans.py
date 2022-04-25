from collections import Counter

N = int(input())
A = list(map(int, input().split()))

A.sort()
counter = Counter(A)

ans = sum(counter[i] * counter[i // a] for a in A for i in range(a, A[-1] + 1, a))
print(ans)


