from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        anotha_one = 0
        while True:
            anotha_one = nums[anotha_one]
            slow = nums[slow]
            if slow == anotha_one:
                return anotha_one
            
    

s = Solution()
l1 = [1, 2, 4, 3, 2]

print(s.findDuplicate(l1))
