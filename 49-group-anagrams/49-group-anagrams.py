# Approach used: using count of char as key and its value as list of strings 
# Time complexity: O(MN)
# Space complexity: O(MN)

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 

            for c in s:
                count[ord(c) - ord("a")] +=1 
            res[tuple(count)].append(s)
        return res.values()
