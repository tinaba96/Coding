N = int(input())

bx = set()
index = 1

while True:

    while index in bx:
        index += 1
    print(index, flush=True)
    bx.add(index)

    val = int(input())
    if val == 0:
        exit()
    bx.add(val)




