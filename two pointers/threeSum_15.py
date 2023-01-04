from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):

            # check for duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            begin = i + 1
            end = len(nums) - 1
            target = -nums[i]
            two_sum_sols = self.twoSumSorted(nums, begin, end, target)
            
            for sol in two_sum_sols:
                res.append([nums[i], sol[0], sol[1]])
        return res

    def twoSumSorted(self, sorted_nums, begin, end, target):
        res = set()
        while begin < end:
            sumNum = sorted_nums[begin] + sorted_nums[end]
            if sumNum == target:
                res.add((sorted_nums[begin], sorted_nums[end]))
                end -= 1
            elif sumNum > target:
                end -= 1
            else:
                begin += 1
        return res

s = Solution()
nums =  [-1,0,1,2,-1,-4]
print(s.threeSum(nums))
