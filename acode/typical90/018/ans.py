from math import atan2, cos, pi, sin, sqrt, degrees
T = int(input())
L, X, Y = list(map(int, input().split()))
Q = int(input())

for e in range(Q):
    E = int(input())
    angle= E/T*2*pi
    pz = L/2-L/2*cos(angle)
    py = -L/2*sin(angle)
    d = sqrt((Y-py)**2+X**2)
    w = atan2(pz, d)
    #print(w/pi*180)
    print(degrees(w))
    #print(w * 360 / 2 / pi)

