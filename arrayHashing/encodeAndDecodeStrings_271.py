class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encode_list = []
        
        for s in strs:
            encode_list.append(str(len(s)))
            encode_list.append("#")
            encode_list.append(s)

        return ''.join(encode_list)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, s):
        ptr = 0
        
        words = []
        while(ptr < len(s)):
            delimeter = s.find("#", ptr, len(s))
            length = int(s[ptr : delimeter])
            ptr = delimeter + 1
            decoded = s[ptr : ptr + length]
            ptr = length + ptr
            words.append(decoded)
        
        return words


s = Solution()
words = ["neet", "code"]
print(s.encode(words))
print(s.decode(s.encode(words)))


