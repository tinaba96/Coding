S = str(input())
a, b = list(map(int, input().split()))

print(S[:a-1]+S[b-1]+S[a:b-1]+S[a-1]+S[b:])


