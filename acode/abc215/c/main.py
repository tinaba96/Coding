import collections

S, k = list(map(str, input().split()))

K = int(k)
ans = []
A = []
for s in range(len(S)):
    A.append(S[s])

d = 1 
A = sorted(A)
c = collections.Counter(A)
for val in c.values():
    d *= val
print(d)
if len(S) >= 8:
    t = K // (5040+1)
    if t != 0:
        ans.append(A[t])
        A.pop(A.index(A[t]))
    else:
        ans.append(A[0])
        A.pop(A.index(A[0]))

    K = K - 5040*t

if len(S) >= 7:
    t = K // (720+1)
    if t != 0:
        ans.append(A[t])
        A.pop(A.index(A[t]))
    else:
        ans.append(A[0])
        A.pop(A.index(A[0]))
    K = K - 720*t

if len(S) >= 6:
    t = K // (120+1)
    if t != 0:
        ans.append(A[t])
        A.pop(A.index(A[t]))
    else:
        ans.append(A[0])
        A.pop(A.index(A[0]))
    K = K - 120*t

if len(S) >= 5:
    t = K // (24+1)
    if t != 0:
        ans.append(A[t])
        A.pop(A.index(A[t]))
    else:
        ans.append(A[0])
        A.pop(A.index(A[0]))
    K = K - 24*t
        
if len(S) >= 4:
    t = K // ((6+1)//d)
    if t != 0:
        ans.append(A[t])
        A.pop(A.index(A[t]))
    else:
        ans.append(A[0])
        A.pop(A.index(A[0]))
    K = K - 6*t

if len(S) >= 3:
    t = K // ((2+1)//d)
    if t != 0:
        ans.append(A[t])
        A.pop(A.index(A[t]))
    else:
        ans.append(A[0])
        A.pop(A.index(A[0]))
    K = K - 2*t
    
if len(S) >= 2:
    t = K // ((1+1)//d)
    if t != 0:
        ans.append(A[t])
        A.pop(A.index(A[t]))
    else:
        ans.append(A[0])
        A.pop(A.index(A[0]))
    K = K - 1*t


    ans.append(A[0])
print(ans)

