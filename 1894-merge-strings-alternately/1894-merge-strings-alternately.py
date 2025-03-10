class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        newstr=''
        let's probably pick the first word and iterate 
        while i<len(word1):
        when i = 0 
        newstr+=w1[i]
        if i<len(word2):
        newstr+=w2 [i]

        if i<len(word2):
            newstr+=word2[i+1:]
        '''
        result = ""
        i=0
        while i<len(word1):
            result += word1[i]
            if i<len(word2):
              result += word2[i]
            i += 1
        if i<len(word2):
            result += word2[i:]
        return result
        