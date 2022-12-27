from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurances = {}
        for n in nums:
            if n in occurances:
                occurances[n] += 1
            else:
                occurances[n] = 1
        inv_occurances = {}
        for key, value in occurances.items():
            if value in inv_occurances:
                inv_occurances[value].append(key)
            else:
                inv_occurances[value] = [key]
                
        res = []
        for i in range(len(nums), 0, -1):
            if i in inv_occurances:
                for freq in inv_occurances[i]:
                    res.append(freq)
                    if len(res) == k:
                        return res
        

s = Solution()
nums = [1]
k = 1
print(s.topKFrequent(nums, k))