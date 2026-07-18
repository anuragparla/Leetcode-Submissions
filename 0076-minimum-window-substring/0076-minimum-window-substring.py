class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        min_length = float('inf')
        res = ""
        freq_ct_t = {}
        freq_ct_s = {}
        formed = 0

        for ch in t:
            freq_ct_t[ch] = freq_ct_t.get(ch, 0) + 1

        required = len(freq_ct_t)  # number of unique chars needed

        for r in range(len(s)):
            ch = s[r]
            if ch in freq_ct_t:
                freq_ct_s[ch] = freq_ct_s.get(ch, 0) + 1
                # just reached the required count for this char
                if freq_ct_s[ch] == freq_ct_t[ch]:
                    formed += 1

            # shrink the window while it's valid
            while formed == required:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    res = s[l:r+1]

                left_ch = s[l]
                if left_ch in freq_ct_t:
                    freq_ct_s[left_ch] -= 1
                    # dropped below required count
                    if freq_ct_s[left_ch] < freq_ct_t[left_ch]:
                        formed -= 1
                l += 1

        return res
        