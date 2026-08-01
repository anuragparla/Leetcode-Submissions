class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):

            curr = root 
            for i in range(j,len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1,child):
                            return True
                    return False

                
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.is_word
        
        return dfs(0,self.root)
            

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)