class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        ndx = 0
        seen = set()
        for i, c in enumerate(s):
            if c in seen:
                ndx = i
                seen.clear()
                seen.add(c)
            else:
                seen.add(c)

            length = i - (ndx - 1)
            if length > longest_length:
                longest_length = length

        return longest_length




s = Solution()
string = "dvdf"
print(s.lengthOfLongestSubstring(string))