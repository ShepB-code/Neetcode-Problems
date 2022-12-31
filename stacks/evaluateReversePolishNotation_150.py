from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            try:
                s.append(int(t))
            except:        
                op2 = int(s.pop())
                op1 = int(s.pop())
                if t == '+':
                    res = op1 + op2
                elif t == '-':
                    res = op1 - op2
                elif t == '*':
                    res = op1 * op2
                else:
                    res = op1 / op2
                s.append(res)
        
        return int(s.pop())


            

s = Solution()
calc = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(s.evalRPN(calc))