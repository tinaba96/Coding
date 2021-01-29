N = int(input())
A = list(map(int, input().split()))


tmp = [0]*max(A)

num = 0
leng = 0

for i in range(max(A)):
    ans = min(A)*len(A)
    lengt = 0
    for j in range(len(A)):
        A[j] -= 1
    num += 1
    for t in range(len(A)):
        #print(A)
        if A[t] >= 1:
            leng += 1
            #print('leng',leng)
            lengt = max(lengt,leng)
        else:
            flag = False
            leng = 0
    #print('lengt',lengt)
    tmp[i] = max(ans, lengt*(num+1))

#print(tmp)

print(max(tmp))
