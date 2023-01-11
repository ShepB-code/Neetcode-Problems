from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i in range(0, len(nums)):
            comp = target - nums[i]
            if comp in complements:
                return [i, complements[comp]]
            else:
                complements[nums[i]] = i
        return []

