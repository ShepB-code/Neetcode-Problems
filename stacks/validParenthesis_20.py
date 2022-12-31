class Solution:
    def isValid(self, s: str) -> bool:
        comp = {']': '[', ')': '(', '}': '{'}

        stack = []
        for c in s:
            if c in comp: # ] [
                if len(stack) == 0:
                    return False
                if stack.pop() != comp[c]:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
