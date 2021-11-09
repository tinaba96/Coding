x = str(input())
ans = ''
k = 0
for i in range(len(x)):
    if x[i] == '.':
        ans = x[:i]
        k = int(x[i+1])
        break
    #ans += x[i]
    #print(ans)

if k >= 5:
    print(int(ans)+1)
else:
    print(ans)
