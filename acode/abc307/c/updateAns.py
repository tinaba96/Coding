# 入力Ha,Wa
Ha, Wa = map(int, input().split())
# シートAの黒いマスの座標を保存
black_A = set()
for i in range(Ha):
    # 入力A
    A = list(input())
    for j in range(Wa):
        # 黒いマス="#"だったら座標を保存
        if A[j] == "#":
            black_A.add((i, j))

# 入力Hb,Wb
Hb, Wb = map(int, input().split())
# シートBの黒いマスの座標を保存
black_B = set()
for i in range(Hb):
    B = list(input())
    for j in range(Wb):
        # 黒いマス="#"だったら座標を保存
        if B[j] == "#":
            black_B.add((i, j))

# 入力Hx,Wx
Hx, Wx = map(int, input().split())
# シートXの黒いマスの座標を保存
black_X = set()
for i in range(Hx):
    X = list(input())
    for j in range(Wx):
        # 黒いマス="#"だったら座標を保存
        if X[j] == "#":
            black_X.add((i, j))

# Aの黒いマスの座標を-Hx~Hxの範囲で移動する
moved_black_A = []
for i in range(-Ha, Hx):
    for j in range(-Wa, Wx):
        a = set()
        for k in black_A:
            a.add((k[0]+i, k[1]+j))
        moved_black_A.append(a)

# Bの黒いマスの座標を-Hx~Hxの範囲で移動する
moved_black_B = []
for i in range(-Hb, Hx):
    for j in range(-Wb, Wx):
        b = set()
        for k in black_B:
            b.add((k[0]+i, k[1]+j))
        moved_black_B.append(b)


for i in moved_black_A:
    for j in moved_black_B:
        # AとBの黒いマスの座標とXの黒いマスが等しければ、
        # Yesと出力する
        if i|j == black_X:
            print("Yes")
            exit()
print("No")

