class Solution:
    def isPalindrome(self, s: str) -> bool:
        beg: int = 0
        end: int = len(s) - 1
        while beg < end:
            currBeg = s[beg]
            currEnd = s[end]
            # make sure beg and end are numeric
            if s[beg].isalnum() and s[end].isalnum():
                # convert both to lower
                currBeg = s[beg].lower()
                currEnd = s[end].lower()
                if(currBeg != currEnd):
                    return False
                    
                beg += 1
                end -= 1
            else:

                if not s[beg].isalnum():
                    beg += 1
                if not s[end].isalnum():
                    end -= 1
                
        

        return True



s = Solution()
test = "A man, a plan, a canal: Panama"
test2 = "0P"
print(s.isPalindrome(test2))