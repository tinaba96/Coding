X = str(input())

M = int(input())

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out#int out


ma = 0
for t in X:
    ma = max(ma, int(t))
    

ans = 0
start = ma
end = 1000000000000000
while True:
    mid = (start + end)//2
    if Base_n_to_10(X,mid) <= M:
        #ans += mid - ma
        start = mid
        flag = True
    else:
        end = mid
        flag = False

    if abs(start-end)==1:
        break

if flag:
    ans = mid-ma
else:
    ans = mid - ma-1

#print(Base_10_to_n(22,3))
#print(Base_n_to_10(str(22),3))


print(ans)


