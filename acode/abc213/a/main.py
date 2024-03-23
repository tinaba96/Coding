A, B =list(map(int, input().split()))


for i in range(256):
    if A ^ i == B:
        print(i)

