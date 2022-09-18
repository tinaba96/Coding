N = int(input())

ans = [] 

i = N

while True:
    ans.append(N)
    if i == 0:
        break
    i = (i-1)&N

print(ans)


