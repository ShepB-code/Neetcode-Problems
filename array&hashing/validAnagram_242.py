class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        for c in s:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1

        for c in t:
            if c in letters:
                letters[c] -= 1
                if letters[c] == 0:
                    letters.pop(c)
            else:
                return False

        return len(letters) == 0