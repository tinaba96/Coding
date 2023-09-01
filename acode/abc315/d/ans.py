H, W = map(int, input().split())
C = [[*map(lambda c: ord(c) - ord('a'), input())] for _ in range(H)]

row = [[0]*26 for _ in range(H)]
col = [[0]*26 for _ in range(W)]
row_tot = [0]*H
col_tot = [0]*W
row_k = [0]*H
col_k = [0]*W

for h in range(H):
    for w in range(W):
        c = C[h][w]
        row_k[h] += row[h][c] == 0
        col_k[w] += col[w][c] == 0
        row_tot[h] += 1
        col_tot[w] += 1
        row[h][c] += 1
        col[w][c] += 1

row_del = [0]*H  # [x]=ture: x は削除済み
col_del = [0]*W


def del_exe(h, w):
    if row_del[h] or col_del[w]:
        return
    c = C[h][w]
    row[h][c] -= 1
    col[w][c] -= 1
    row_tot[h] -= 1
    col_tot[w] -= 1
    row_k[h] -= row[h][c] == 0
    col_k[w] -= col[w][c] == 0


update = True
while update:
    update = False
    del_row, del_col = [], []  # 削除対象を収集

    for h in range(H):
        if not row_del[h] and row_tot[h] >= 2 and row_k[h] == 1:
            del_row.append(h)

    for w in range(W):
        if not col_del[w] and col_tot[w] >= 2 and col_k[w] == 1:
            del_col.append(w)

    for h in del_row:
        for w in range(W):
            del_exe(h, w)
        row_del[h] = update = True

    for w in del_col:
        for h in range(H):
            del_exe(h, w)
        col_del[w] = update = True

ans = 0
for h in range(H):
    for w in range(W):
        ans += not (row_del[h] or col_del[w])
print(ans)

