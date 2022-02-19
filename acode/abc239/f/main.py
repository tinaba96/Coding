N, M = list(map(int, input().split()))
D = list(map(int, input().split()))

for m in range(M):
    A, B = list(map(int, input().split()))
    D[A-1] -= 1
    D[B-1] -= 1

arr = []

for i in range(N):
    if D[i] != 0:
        arr.append((i, D[i]))

#print(arr)
s_arr = sorted(arr, key=lambda x:x[1], reverse=True)
print(s_arr)

def build_bridge(f, s, B):
    for i in range(len(s_arr)):
        if s != 0 and f != 0:
            B.append((f,s))
        if f == 0:
            f = s_arr[i][0]
        else:
            s = s_arr[i][0]

        s_arr[i][1] -= 1
        if s_arr[i][0] == 0:
            s_arr.remove(s_arr[i])
        if len(s_arr) == 0:
            if len(B) == N-M-1:
                print(B)
                exit()
            return
        build_bridge(f, s, B)
            





B = []
build_bridge(0, 0, B)

