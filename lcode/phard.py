
from collections import deque
from typing import List


class Solution:
    #4
    def findMedianSortedArrays(self, nums1: List[int], nums2:List[int]) -> float:

        oi = 0
        ti = 0
        merged = []

        while oi < len(nums1) and ti < len(nums2):
            if nums1[oi] < nums2[ti]:
                merged.append(nums1[oi])
                oi += 1
            else:
                merged.append(nums2[ti])
                ti += 1

        if oi < len(nums1):
            merged.extend(nums1[oi:])
        if ti < len(nums2):
            merged.extend(nums2[ti:])

        print(merged)
        if len(merged)%2 != 0:
            return float(merged[len(merged)//2])
        else:
            return float((merged[len(merged)//2-1] + merged[len(merged)//2])/2)

    def median(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError
        
        imin, imax, half_len = 0, m, (m+n+1)//2
        while imin <= imax:
            i = (imin + imax)//2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m+n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0
    #modifiedans
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        #(m+n+1)の+1は全体の長さが奇数だったっ場合に、中間線の一個前を中間のノードにするため
        #+1しない場合は、中間線の一個後のノードを中間ノードとして扱えば良いと思われる。
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0

if __name__ == "__main__":
    s = Solution()
    #print(s.findMedianSortedArrays([1,2], [3,4]))
    print(s.median([1,2], [3,4]))


