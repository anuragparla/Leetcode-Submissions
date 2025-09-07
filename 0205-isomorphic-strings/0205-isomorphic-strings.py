class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        '''
        Method 1: using Hash map and a hash set
        Time: O(N)
        Space: O(N)
        '''
        # s_to_t_map = dict()
        # set_of_t_chars = set()

        # for i in range(len(s)):
        #     if s[i] not in s_to_t_map:
        #         if t[i] not in set_of_t_chars:
        #             s_to_t_map[s[i]] = t[i]
        #             set_of_t_chars.add(t[i])
        #         else:
        #             return False
        #     else:
        #         if s_to_t_map[s[i]] != t[i]:
        #             return False
        
        # return True
        '''
        Method 2: Using Single Hashmap
        Time: O(N)
        Space: O(N)
        '''
        char_to_char_map = dict()
        for i in range(len(s)):
            if s[i]+'_s' not in char_to_char_map:
                char_to_char_map[s[i]+'_s'] = t[i]
            else:
                if char_to_char_map[s[i]+'_s'] != t[i]:
                    return False

            if t[i]+'_t' not in char_to_char_map:
                char_to_char_map[t[i]+'_t'] = s[i]
            else:
                if char_to_char_map[t[i]+'_t'] != s[i]:
                    return False
        return True




        