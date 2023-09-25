def I():
    h, w = map(int, input().split())
    s = 0
    for _ in range(h):
        s = (s << 20) + int(input().replace("#", "1").replace(".", "0"), 2)  # 20 is important to handle the case below
    return s // (s & -s)

a, b, x = I(), I(), I()
#print(bin(a))
#print(bin(b))
#print(bin(x))
for i in range(300): # 200 is also ok
    #print(bin(b << i))
    if a | (b << i) == x or (a << i) | b == x:
        print("Yes")
        break
else:
    print("No")


# https://atcoder.jp/contests/abc307/editorial/6691

'''
if 
s = (s << 10) + int(input().replace("#", "1").replace(".", "0"), 2) 
it will be WA like below

input
3 10
..........
#.........
..........
3 10
..........
##########
..........
3 10
.......###
#######...
..........

output
Yes
'''

