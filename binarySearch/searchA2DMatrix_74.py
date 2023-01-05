from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:      

        # find which row it is on
        beg_row = 0
        end_row = len(matrix) - 1
        found_row = False

        while beg_row <= end_row and not found_row:
            middle_row = (beg_row + end_row) // 2
            if target > matrix[middle_row][-1]:
                beg_row = middle_row + 1
            elif target < matrix[middle_row][0]:
                end_row = middle_row - 1
            else:
                found_row = True

        if found_row:
            beg = 0
            end = len(matrix[middle_row]) - 1
            while beg <= end:
                middle = (beg + end) // 2
                if target == matrix[middle_row][middle]:
                    return True
                elif target > matrix[middle_row][middle]:
                    beg = middle + 1
                else:
                    end = middle - 1
        
        
        return False


s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(s.searchMatrix(matrix, target))