from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg = 0
        end = len(nums) - 1
        
        while beg <= end:
            middle = (beg + end) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                beg = middle + 1
            else:
                end = middle - 1
            
        return -1
        
s = Solution()
nums = [-1,0,3,5,9,12]
target = 2
print(s.search(nums, target))