from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        beg = 0
        end =  len(height) - 1
        max_area = 0

        while beg < end:
            max_area = max(min(height[beg], height[end]) * (end - beg), max_area)

            # increment pointer with smallest height
            if height[beg] < height[end]:
                beg += 1
            else:
                end -= 1

        return max_area

s = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(s.maxArea(height))