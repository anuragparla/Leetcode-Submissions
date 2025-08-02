class Trie:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.isEnd = False


    def __init__(self):
        self.root = self.TrieNode()


    def insert(self, word: str) -> None:
        # used to traverse the trie
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            if curr.children[ord(c)- ord('a')] is None:
                curr.children[ord(c)- ord('a')] = self.TrieNode()
            curr = curr.children[ord(c)- ord('a')]
        curr.isEnd = True
         
        return

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            if curr.children[ord(c)- ord('a')] is None:
                return False
            
            curr = curr.children[ord(c)- ord('a')]

        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            if curr.children[ord(c)- ord('a')] is None:
                return False
            curr = curr.children[ord(c)- ord('a')]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)