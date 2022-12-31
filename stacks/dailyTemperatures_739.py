from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []
        for i, t in enumerate(temperatures):
            while s and t > s[-1][0]:
                stackI = s.pop()[1]
                res[stackI] = (i - stackI)
            s.append([t, i])
        return res




s = Solution()
temps = [73,74,75,71,69,72,76,73]
print(s.dailyTemperatures(temps))