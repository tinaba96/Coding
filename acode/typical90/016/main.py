N = int(input())
A = list(map(int, input().split()))

ans = 10000

A.sort(reverse=True)

'''
for i in range(10000):
    if i*A[0] < N:
        continue
    else:
'''

'''
for i in range(10000):
    #print('check1')
    val1 = i*A[0]
    if val1 > N:
        break
    for j in range(1000):
        #print('check2')
        if i+j >= 10000:
            break
        val2 = j*A[1]
        if val1+val2 > N:
            break
        for k in range(10000):
            #print('check3')
            if i+j+k >= 10000:
                break
            val3 = k*A[2]
            if val1+val2+val3 > N:
                break
            if val1+val2+val3 == N:
                ans = min(ans, i+j+k)
                break
'''


for i in range(10000):
    #print('check1')
    val1 = i*A[0]
    for j in range(10000-i):
        #print('check2')
        val2 = j*A[1]
        if val1+val2 > N:
            break
        elif (N-val1-val2)%A[2] == 0:
            k = (N-val1-val2)//A[2]
            ans = min(ans, i+j+k)
            

            
print(ans)


# the difference between "break" and "continue" made me confused which led to WA


#print(A)


