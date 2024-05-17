L, R = list(map(int, input().split()))
S = str(input())


clip = S[L-1:R]

rev = clip[::-1]

print(S[:L-1]+rev+S[R:])



