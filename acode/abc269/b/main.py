ans = []
for i in range(10):
    S = str(input())
    for j in range(10):
        if S[j] == '#':
            ans.append((i,j))

#print(ans)
print(ans[0][0]+1, ans[-1][0]+1)
print(ans[0][1]+1, ans[-1][1]+1)








