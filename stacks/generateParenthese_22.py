from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
       
        s = []
        r = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                r.append("".join(s))
                return
            
            if openN < n:
                s.append('(')
                backtrack(openN + 1, closeN)
                s.pop()
            
            if closeN < openN:
                s.append(')')
                backtrack(openN, closeN + 1)
                s.pop()
        
        backtrack(0, 0)      
        return r  

s = Solution()
n = 5
print(s.generateParenthesis(n))
