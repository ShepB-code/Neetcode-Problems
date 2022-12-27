from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            sorted_version = ''.join(sorted(s))
            if sorted_version in hashmap:
                hashmap[sorted_version].append(s)
            else:
                hashmap[sorted_version] = [s]

        res = []
        for v in hashmap.values():
            res.append(v)
            
        return res

