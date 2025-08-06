class Solution:
    def customSortString(self, order: str, s: str) -> str:
        if len(order) == 0 or order is None or len(s) == 0 or s is None:
            return ''
        #create a map of charcter and its count 
        char_to_freq_map = dict()
        for i in s:
            if i not in char_to_freq_map:
                char_to_freq_map[i] = 1 
            else:
                char_to_freq_map[i] += 1
        print(char_to_freq_map)
        s1 = ''
        s2 = ''
        #iterate over order 
        for c in order:
            if c in char_to_freq_map:
                s1 += c * char_to_freq_map[c]
        for c in s:
            if c not in s1:
                s1 += c * char_to_freq_map[c]
        return s1