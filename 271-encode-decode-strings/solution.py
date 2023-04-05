class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if len(strs) == 0:
            return chr(258)
        delimiter = chr(257)
        
        return delimiter.join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if s == chr(258):
            return []
        
        return s.split(chr(257))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
