N = int(input())

one = []

T = str(bin(N))

for i in range(len(T)-1, 1, -1):
    if T[i] == '1':
        one.append(len(T)-i-1)

#print(2 << 1)

for j in range(2**len(one)):
    ans = 0
    #print(bin(j))
    for k in range(len(str(bin(j)))-2):
        if 1 << k & j:
            #print('add: ',k)
            #print(bin(j))
            #print('asfd')
            ans += 2**one[k]
    print(ans)

#print(bin(N))
#print(one)
#rint(len(one))


