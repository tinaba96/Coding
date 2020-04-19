#1007
class Solution:
    import collections
    import copy
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        C = copy.copy(A)
        C.extend(B)
        cC = collections.Counter(C)
        ans = 0
        if  cC.most_common()[0][1] < len(A):
            return -1
        else:
            n = cC.most_common()[0][0]
            if A.count(n) > B.count(n):
                for i in range(len(A)):
                    if n != A[i]:
                        if n == B[i]:
                            ans += 1
                        else:
                            return -1
            else:
                for i in range(len(B)):
                    if n != B[i]:
                        if n == A[i]:
                            ans += 1
                        else:
                            return -1
        return ans

    #faster answer
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            """
            Return min number of swaps
            if one could make all elements in A or B equal to x.
            Else return -1.
            """
            # how many rotations should be done
            # to have all elements in A equal to x
            # and to have all elements in B equal to x
            rotations_a = rotations_b = 0
            for i in range(n):
                # rotations coudn't be done
                if A[i] != x and B[i] != x:
                    return -1
                # A[i] != x and B[i] == x
                elif A[i] != x:
                    rotations_a += 1
                # A[i] == x and B[i] != x
                elif B[i] != x:
                    rotations_b += 1
            # min number of rotations to have all
            # elements equal to x in A or B
            return min(rotations_a, rotations_b)

        n = len(A)
        rotations = check(A[0])
        # If one could make all elements in A or B equal to A[0]
        if rotations != -1 or A[0] == B[0]:
            return rotations
        # If one could make all elements in A or B equal to B[0]
        else:
            return check(B[0])


'''
２種類の解法の計算時間における、自分なりの分析
上：1212ms
下：1160ms
ループによる計算時間はほとんど差がない
上のコードの実装過程で用いてたと思われる余分なコードが2行あった
cA = collections.Counter(C)
cB = collections.Counter(C)
これを削除したら、計算速度が改善した
上の改善：1164ms
つまり、余分な計算をしていたため、上のコードの方が遅かったと思われる。
ただ、いずれにせよ、O(n)であることには変わりないため、大きな問題ではないと思われる。

上の実装の余分な部分といえば、全ての要素の個数をカウントしていることである。
どっちしても、全ての要素をforループで確認しているので、下の実装のように、A[0]とB[0]だけをみて全要素確認する方が効率が良いと思われる。
とにかく個数が最大の物を探す必要はない。

しかし、下のコードはB[0]に求める値があった場合、計算量は2nになるが、上のコードはnで終わる。
したがって、最悪のケースでは上のコードの方が良く、最良のケースでは下のコードの方が良いと考えられる。

と思ったが、collections.Counterで計算量2n、count()で計算量n要しているため、上のコードの計算量は5n、下のコードの計算量は2nであると思われる。most_common()の計算量もかかる。ソートなので、早くてもO(nlogn)？

以上から、計算量の面では下の実装の方が賢い方法であると言える。
'''

#809
class Solution:
    import collections
    def expressiveWorld(self, S: str, words: List[int]) -> int:
        for ele in words:
            flag = True
            if S[0] != ele[0]:
                flag = False
                break
            group = 0
            for i in range(1, len(S)):
                if S[i] == S[i-1]:
                    group += 1
                else:
                    if ele[i] != ele[i-1]:
                        if S[i] != ele[i]:
                            flag = False
                            break
            if flag == True:
                
        
        
        


        c = collections.Counter
        cnt = c.Counter(S)
        for ele in words:
            for i in range(len(cnt)):

    #ans 
    def expressiveWords(self, S, words):
        def RLE(S):
            return zip(*[(k, len(list(grp)))
                         for k, grp in itertools.groupby(S)])

        R, count = RLE(S)
        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R: continue
            ans += all(c1 >= max(c2, 3) or c1 == c2
                       for c1, c2 in zip(count, count2))

        return ans



























