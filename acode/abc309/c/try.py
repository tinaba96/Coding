# ソートしたいmapの作成
my_map = {'c': 3, 'a': 1, 'b': 2}

# キーをソートしたリストを作成
sorted_keys = sorted(my_map.keys())

# ソート済みのmapを作成
sorted_map = {}
for key in sorted_keys:
    sorted_map[key] = my_map[key]

# ソート済みのmapの表示
print(sorted_map)


for e in sorted_map:
    print(e)

