class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            print(row)

        print("\n")
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue

                val = int(board[row][col])
                board[row][col] = "#"

                if str(val) in board[row]:
                    return False

                board[row][col] = str(val)
                
                for i in range(len(board)):
                    if board[i][col] == "." or i == row:
                        continue
                    if board[i][col] == board[row][col]:
                        return False
                 
                bx_r_idx, bx_c_idx = row - (row % 3), col - (col % 3)
                
                bx_positions = [
                    (bx_r_idx, bx_c_idx), (bx_r_idx, bx_c_idx + 1), (bx_r_idx, bx_c_idx + 2),
                    (bx_r_idx+1, bx_c_idx), (bx_r_idx+1, bx_c_idx + 1), (bx_r_idx+1, bx_c_idx + 2),
                    (bx_r_idx+2, bx_c_idx), (bx_r_idx+2, bx_c_idx + 1), (bx_r_idx+2, bx_c_idx + 2)
                ]

                for adj_row, adj_col in bx_positions:
                    if board[adj_row][adj_col] == "." or adj_row == row and adj_col == col:
                        continue
                    if board[adj_row][adj_col] == board[row][col]:
                        return False

        return True
                



            
          
                        
                        