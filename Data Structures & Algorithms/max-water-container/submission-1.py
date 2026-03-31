class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxAmount = 0

        l, r = 0, n - 1

        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            maxAmount = max(maxAmount, h * w)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxAmount