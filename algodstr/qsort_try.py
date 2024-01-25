N = int(input())
A = list(map(int, input().split()))

'''
# this is not a quick sort

ans = []

def qs(a):
    if len(a) == 1:
        ans.append(a)
        return 

    r_arr = []
    l_arr = []
    pivot = a[N//2]
    for e in a:
        if e <= pivot:
            l_arr.append(e)
        else:
            r_arr.append(e)

    qs(l_arr)
    qs(r_arr)


qs(A)


print(ans)
'''

def qs(a, l, r):
    pl = l # left cursor
    pr = r # right cursor
    pivot = a[(l+r)//2]

    while pl < pr:
        while a[pl] < pivot: pl += 1
        while a[pr] > pivot: pr -= 1
        if pl <= pr:  #  whether is has "=" or not, will effect the array whose length is odd or even.
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

        # these are not neccesary, I think
        #if l < pr: qs(a, l, pr)
        #if pl < r: qs(a, pl, r)
        qs(a, l, pr)
        qs(a, pl, r)

qs(A, 0, N-1)

print(A)

