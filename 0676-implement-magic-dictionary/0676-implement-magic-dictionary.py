class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False
class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def buildDict(self, dictionary: List[str]) -> None:
        
        for word in dictionary:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_word = True
     
        

    def search(self, searchWord: str) -> bool:
        def dfs(idx,node, changes):
            if idx == len(searchWord):
                return node.is_word and changes == 1 
            c = searchWord[idx]

            if c in node.children:
                if dfs(idx+1,node.children[c], changes):
                    return True
            if changes == 0:
                for key,child in node.children.items():
                    if key !=c:
                        if dfs(idx+1, child, changes=1):
                            return True
            return False
        
        return dfs(0,self.root, 0)
                 

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)