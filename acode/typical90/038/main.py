from collections import defaultdict

A, B = list(map(int, input().split()))

large = 10**18


def fac(x):
    r = defaultdict(int)
    for i in range(2, x):
        while x % i == 0:
            x /= i
            r[i] += 1
    return r


        


            
        
    







