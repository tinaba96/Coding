N = int(input())
S = str(input())

ans = ['0']

ind = 0

for i in range(N):
    if S[i] == 'L':
        ans.insert(ind, str(i+1))
    else:
        ind += 1
        ans.insert(ind, str(i+1))

print(' '.join(ans))





