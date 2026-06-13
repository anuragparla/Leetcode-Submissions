class Solution:
    def finalString(self, s: str) -> str:
        res = ''
        for idx,wrd in enumerate(s):
            if wrd == 'i':
                res = res[:idx][::-1]
            else:
                res += wrd
        return res


        