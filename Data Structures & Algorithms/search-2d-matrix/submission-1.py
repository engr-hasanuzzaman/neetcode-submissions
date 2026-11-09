class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # find the potential rows first
        s_row, e_row = 0, len(matrix) - 1
        # print(s_row, e_row)
        while s_row <= e_row:
            mid = s_row + (e_row - s_row) // 2
            # print(mid)
            if target >= matrix[mid][0] and  target <= matrix[mid][-1]:
                break
            elif target > matrix[mid][0]:
                s_row = mid + 1
            else:
                e_row = mid - 1
        
        # print("target row is", mid)
        # do binary search in target row 
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid_col = left + (right - left) // 2
            if matrix[mid][mid_col] == target:
                return True
            if target > matrix[mid][mid_col]:
                left = mid_col + 1
            else:
                right = mid_col - 1
        
        return False

         