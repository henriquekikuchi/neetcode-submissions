class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1) ## 2
        n = len(nums2) ## 1

        total = m + n ## 3
        half = (total + 1) // 2 ## 3 + 1 = 4 // 2 = 2

        if m > n:## true
            nums1, nums2 = nums2, nums1 ## [3], [1,2]
            m, n = n, m ## 1, 2

        left = 0
        right = m ## 1

        while left <= right:
            i = (left + right) // 2 ## 0 + 1 // 2 = 0
            j = half - i ## 2 - 0 = 2

            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf") 

            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf") 

            if left1 <= right2 and left2 <= right1:
                x = max(left1,left2)
                y = min(right1, right2)

                if total % 2 == 1:
                    return x
                else:
                    return (x + y) / 2
            
            if left1 > right2:
                right = i - 1
            else:
                left = i + 1
                

