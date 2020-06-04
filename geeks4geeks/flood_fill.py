'''

def change_color(mat, i, j):
    if i < 0 or i > w-1:
        return 0
    if j < 0 or j > h-1:
        return 0
    if mat[i][j] != before_color:
        return 0
    else:
        mat[i][j] = col
    change_color(mat, i, j+1)
    change_color(mat, i+1, j)
    change_color(mat, i, j-1)
    change_color(mat, i-1, j)




T = int(input())

for _ in range(T):

    w, h = list(map(int, input().split()))

    el = list(map(int, input().split()))

    mat = [[None]*h for _ in range(w)]




    for i in range(0, w*h, h):
        for j in range(h):
            mat[i//h][j] = el[i+j]


    x, y, col = list(map(int, input().split()))

    before_color = mat[x][y]


    change_color(mat, x, y)

    ans = []

    for i in range(w):
        for ele in mat[i][:]:
            ans.append(str(ele))

    result = ' '.join(ans)
    print(result)

'''



#anotherans
def search(x,y):
    global a,e,c
    for i,j in [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]:
        if a[i][j]!=-1:
            if a[i][j]==c:
                a[i][j]=e
                search(i,j)


for i in range(int(input())):
    n,m=[int(i) for i in input().split()]
    b=input().split()
    k=input().split()
    x,y,e=int(k[0])+1,int(k[1])+1,k[2]
    i=0
    a=[[-1]*(m+2)] #一行分用意
    #print('before: ', a)
    for j in range(m-1,n*m,m):
        a.append([-1]+b[i:j+1]+[-1])
        i=j+1
    a.append([-1]*(m+2)) #次々に行を追加
    #print(a)
    c=a[x][y]
    a[x][y]=e
    search(x,y)
    #for i in a[1:-1][:]:
    for i in a[1:-1]:
        print(*i[1:-1],end=' ') #*がないと['0', '5', '5', '0'] ['5', '5', '5', '5'] ['0', '5', '2', '3']なってしまう。*はアンパックと呼ばれる。
    print()




