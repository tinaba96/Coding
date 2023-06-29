# video editorial 
# without using string


N = int(input())

ind = 1000

while True:
    if N < ind:
        w = ind // 1000
        ans = N//w*w
        break

    ind *= 10


print(ans)



