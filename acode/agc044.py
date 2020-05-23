#A
'''
T = int(input())

for i in range(T):
    N, A, B, C, D = list(map(int, input().split()))
    ans = 0

    def coins(val, coin):
        if val == N:
            if coin < ans:
                ans = coin
                print(ans)
                return 
        elif val > N:
            val = 1
            coin = D
            return
        else:
            coins(val+1, coin+D)
            coins(val*2, coin+A)
            coins(val*3, coin+B)
            coins(val*5, coin+C)
            coins(val-1, coin+D)

    coins(0, 0)
    print(ans)

'''

T = int(input())

for i in range(T):
    N, A, B, C, D = list(map(int, input().split()))
    val = N

    def coins(val, a, b, c, d, ans):
        if val%2 != 0 and val%3 != 0 and val%5 != 0:
            d += 1
            val -= 1
        elif val%2 == 0:
            val /= 2
            a += 1
        elif val%3 == 0:
            val /= 3
            b += 1
        elif val%5 == 0:
            val /= 5
            c += 1
        print(a,b,c,d)


        if val == 0:
            ans = min(ans, A*a+B*b+C*c+D*d)

            return ans
        else:
            coins(val, a, b, c, d, ans)

    print(coins(val, 0, 0, 0, 0, 0))

            



'''
T = int(input())


for i in range(T):
    N, A, B, C, D = list(map(int, input().split()))
    ans = 1001001001
    val = 0

    for a in range(N//2+1):
        for b in range(N//3+1):
            for c in range(N//5+1):
                tmp = 2**a*3**b*5**c 
                d = abs(N - tmp)
                ans = min(ans, a*A+b*B+c*C+(d+1)*D)
                #print(ans)

    print(ans)

                   


#B
N = int(input())
P = list(map(int, input().split()))

'''






#C

