N, Q= list(map(int, input().split( )))
X = []
for i in range(Q):
    X.append(int(input()))

integers = [i+1 for i in range(N)]

int_to_loc = dict(zip(integers, integers))
loc_to_int = dict(zip(integers, integers))


for xi in X:
    xi_loc = int_to_loc[xi]
    if xi_loc == N:
        right_loc = xi_loc-1
    else:
        right_loc = xi_loc+1
    right_int = loc_to_int[right_loc]

    int_to_loc[xi] = right_loc
    loc_to_int[right_loc] = xi

    int_to_loc[right_int] = xi_loc 
    loc_to_int[xi_loc] = right_int

    #print(int_to_loc)
    #print(loc_to_int)
    #print()


res = ""
for i in loc_to_int.values():
    res += f" {i}"
print(res[1:])
