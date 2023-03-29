# Time complexity : O(N)
# Space complexity : O(1) but O(N) if we need to support to unicode characters
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict1 = dict()
        for i in s:
            if i in dict1:
                dict1[i] +=1 
            else:
                dict1[i] = 1
        for j in t:
            if j in dict1:
                dict1[j] -=1
                if dict1[j] <0:
                    return False 
            else:
                return False 
        for v in dict1.values():
            if v != 0:
                return False
        return True 
