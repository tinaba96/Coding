a = 30  # 関数の中とは無関係
visit = [1, 2]
def f():
    print(visit)
    #print(a)  # ここで30になったりはしない（この時点でエラー）
    visit = [5, 43]
    #a = 40   # これがある限りaはローカル変数
    #print(a)  # 40が出たりはしない（）
f()


'''
a = 20
def f2(a):
    print(a)
    a = 10
    print(a)
print(a)  # 20
f2(a)      # 20
          # 10
print(a)  # 20
'''
