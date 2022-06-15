from collections import defaultdict
N, K = list(map(int, input().split()))
a = list(map(int, input().split()))

sort = sorted(a)

if K == 1:
    print('Yes')
    exit()

#}mp = [set() for p in range(K+1)]
'''
mp = []
for i in range(K+1):
    mp[i] = defaultdict(int)
'''
#mp = defaultdict(lambda :defaultdict(int))
mp = defaultdict(set)


for j in range(N):
    mp[j%K].add(a[j])

#print(mp)
#print(sort)
for i in range(N):
    if a[i] == sort[i]:
        continue
    else:
        ind = i%K
        if sort[i] not in mp[ind]:
        #if a[i] != sort[i+K]:
            print('No')
            exit()
print('Yes')


# i think this approach is logically correct.
# the only "No" answers is when the two numbers cannot swap.
# if there is a case that cannot swap due the the way we keep some values as set() but answer should be "Yes", those numbers should be same numbers that are not needed to be swapped
# if there are same number of vales or  more than K, it means it will not be "no" becuase of the set() (considered as one even if it has multiple
'''
K: 3
A: 5 1 5 5 8 5
sorted: 1 5 5 5 5 8 (-> "5" of index 4 can be realized anytime even if mp[] only has 1 because all the key in mp has at least one "5" and one of them must have 2 of "5")
-> moreover, there no case that only one key has multiple "5". if some key has multiple, it means all have at leasr one.
'''
# wait above comment is not important

# if mistakenly pass the condition because of set(), it will 100% fail on the other following number. because if the answer is "no":, there will be at least one pair that need to be replaced to be "yes". Thus even though one is mistakenly pass, the other will surely fail.


#therfore, there is no problem that we use set() instead of array.


# above is wrong
# here is the reply from Openchat of Line
'''
すみません、254 Cについてお尋ねしたいのですが、pythonで以下のように入れ替えできる数字をsetのハッシュで持つことで解き、ACしました。（ソート済みのもの比較をすることで可能がどうか調べる方法）
ACする理由をうまく説明できないのですが、正しい解放なのでしょうか。

set()を使用しているため、同じ数字が複数ある場合区別できないのですが、
入れ替えができるグループの中で、同じ数字の２番目を①の部分で見る際、（出力がNoになる場合）実際は二つないのにset()を用いているため通過してしまうケースがあります。
ただその場合は、その分必ず違うグループで通過できなくなるので理論的には正しいと思っています。（出力がNoであるべきところを間違えてYesと出力することはない→Noである場合というのは必ず要素を順番に見ていった時に二箇所以上で、ソート済みのものと差異が出るため。）
この考え方は合っているのでしょうか。ご意見等頂けたら幸いです。よろしくお願い致します。


以下の入力でどうですか。
6 2
1 1 2 1 2 2


“Yes”  になってしまいますね！
ありがとうございます！偶然ACしてしまった感じですかね。
自分の解放が正しいか自信が持てず、反例も全然見つけられず苦戦してました、、
反例探すのって難しいですね、、

'''

