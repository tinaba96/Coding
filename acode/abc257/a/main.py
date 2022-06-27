N, X = list(map(int, input().split()))

base = ord('A')
#print(base)

v = (X-1)//N

print(str(chr(97+v)).upper())


