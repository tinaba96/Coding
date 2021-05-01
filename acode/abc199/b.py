N = input()

A = list(map(int, input().split()))
B = list(map(int, input().split()))

if (min(B)-max(A)+1<=0):
    print('0')
else:
    print(min(B)-max(A)+1)

