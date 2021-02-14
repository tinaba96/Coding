import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

T = int(input())

for t in range(T):
    L, R = list(map(int, input().split()))
    if(L == 0 and R == 0):
        print('1')
    elif(L == R):
        print('0')
    else:
        cnt = 0

        mi = L+L

        #tm = 2*(R-mi)
        tm = combinations_count(R-mi, 2)


        print(tm+2*(R-mi)+1)

        '''
        for i in range(R-L+1):
            for j in range(R-L+1):
                #print('c')
                if(R+j - L+i < R and R+j - L+i > L):
                    cnt += 1
        '''





