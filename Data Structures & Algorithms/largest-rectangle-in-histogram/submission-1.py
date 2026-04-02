class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_value = 0
        stackIdxs = []
        
        heights.append(0)

        for i in range(len(heights)):
            while stackIdxs and heights[stackIdxs[-1]] > heights[i]:
                right = stackIdxs.pop()
                
                if stackIdxs:
                    left = stackIdxs[-1]
                else:
                    left = -1

                width = i - left - 1  

                max_value = max(max_value, width * heights[right] )

            stackIdxs.append(i)
            

        return max_value
