class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        max_water = 0

        while i < j:
            min_h = min(heights[i], heights[j])
            mid = j - i

            area = min_h * mid

            if area > max_water:
                max_water = area

            if min_h == heights[i]:
                i += 1
            else:
                j -= 1

        return max_water
            

            