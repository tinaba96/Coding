import math

R, X, Y = list(map(int, input().split()))

dis = X**2 + Y**2
#dis = math.sqrt(X**2 + Y**2)

#print(dis)


#val = math.ceil(dis)//R
R_ = R**2

val = dis//R_



'''
v = 1
while True:
    if dis <= v*R_:
        break
    else:
        v += 1
    
print(math.ceil(math.sqrt(v)-0.000001))
'''


ans = val

if dis < val*R_:
    ans -= 1

if dis % R_ == 0:
    ans -= 1

a = 1
ans =  ans +1
while True:
    tmp = a*a
    if ans <= tmp:
        break
    else:
        a += 1

print(a)


#print(math.ceil((math.sqrt(ans))))
