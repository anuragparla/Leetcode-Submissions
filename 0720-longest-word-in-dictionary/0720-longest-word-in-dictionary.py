class Solution:
    def longestWord(self, words: List[str]) -> str:
        wordSet = set(words)
        result = ""

        for word in words:
            valid = True

            for i in range(1, len(word)):
                if word[:i] not in wordSet:
                    valid = False
                    break
            
            if valid:
                if len(word) > len(result) or (len(word) == len(result) and word < result): 
                    result = word
        return result
        