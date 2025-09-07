class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        '''
        Method 1: using Hash map and a hash set
        Time: O(N)
        Space: O(N)
        '''
        s_to_t_map = dict()
        set_of_t_chars = set()

        for i in range(len(s)):
            if s[i] not in s_to_t_map:
                if t[i] not in set_of_t_chars:
                    s_to_t_map[s[i]] = t[i]
                    set_of_t_chars.add(t[i])
                else:
                    return False
            else:
                if s_to_t_map[s[i]] != t[i]:
                    return False
        
        return True



        