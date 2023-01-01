from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        beg = 0
        end = len(numbers) - 1
        while beg < end:

            # check to see if we have a two sum
            compBeg = target - numbers[beg]

            if numbers[end] == compBeg:
                return [beg + 1, end + 1]

            # always move end if it's greater than or equal to target
            if numbers[end] > target:
                end -= 1

            else:
                # move whichever one is bigger than the comp of the other
                compEnd = target - numbers[end]
                if numbers[beg] < compEnd:
                    beg += 1

                if numbers[end] > compBeg:
                    end -= 1

        return []

s = Solution()
numbers = [-1000,-1,0,1]
target = 1
print(s.twoSum(numbers, target))



