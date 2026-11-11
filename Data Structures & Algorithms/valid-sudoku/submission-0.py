from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_memo = defaultdict(set)
        col_memo = defaultdict(set)
        box_memo = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                
                # check row
                if num in row_memo[r]:
                    return False
                else:
                    row_memo[r].add(num)


                # check col
                if num in col_memo[c]:
                    return False
                else:
                    col_memo[c].add(num)

                
                # check box, thinks about 3 X 3 matrix
                # will use row to determine begining of the row
                # 0-2 -> 0, 
                # 3 - 5 -> 4
                # 6 - 8 > 6
                box_num = (r // 3 * 3) + c // 3
                
                if num in box_memo[box_num]:
                    return False
                else:
                    box_memo[box_num].add(num)
        return True


                
