#1007
class Solution:
    import collections
    import copy
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        C = copy.copy(A)
        C.extend(B)
        cC = collections.Counter(C)
        cA = collections.Counter(A)
        cB = collections.Counter(B)
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


