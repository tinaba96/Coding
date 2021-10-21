P = list(map(int, input().split()))

alpha = 'abcdefghijklmnopqrstuvwxyz'

ans = []

for i in range(26):
    ans.append(alpha[P[i]-1])

print(''.join(ans))
    


