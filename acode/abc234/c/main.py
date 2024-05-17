K = int(input())

b = bin(K)
ans = []

for i in range(2, len(b)):
    if b[i] == '1':
        ans.append('2')
    else:
        ans.append('0')

print(''.join(ans))


