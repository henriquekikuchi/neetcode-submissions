class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix)
        col_len = len(matrix[0]) 
        
        left = 0
        right = row_len * col_len - 1 

        while left <= right:
            mid = (left + right) // 2
            mid_row = mid // col_len
            mid_col = mid % col_len

            if target > matrix[mid_row][mid_col]:
                left = mid + 1
            elif target < matrix[mid_row][mid_col]:
                right = mid - 1
            else:
                return True

        return False