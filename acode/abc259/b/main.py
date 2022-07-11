import math

a, b, d = list(map(int, input().split()))

x = math.sqrt(a**2 + b**2)

if a == 0:
    if b >= 0:
        th = 90
    else:
        th = 270
else:
    th = math.degrees(math.atan2(b, a))
    #th = math.degrees(math.atan(b/a))

th = th%360
thd = math.radians((th+d)%360)
#print(thd)

#aa = a*math.cos(thd)/math.cos(th)
#bb = b*math.sin(thd)/math.sin(th)
aa = x*math.cos(thd)
bb = x*math.sin(thd)


if str(aa) == '-0.0':
    aa = 0
if str(bb) == '-0.0':
    bb = 0

print(aa, bb)

