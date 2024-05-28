N = int(input())

ans = [] 

i = N

while True:
    ans.append(i)
    if i == 0:
        break
    i = (i-1)&N



for a in ans[::-1]:
    print(a)

