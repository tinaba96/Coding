N = int(input())

g = 0
n = N
if N % 2 != 0:
    n = N-1

while n > 2:
    n /= 2
    g += 1

        
print(g)







print(N-g)




