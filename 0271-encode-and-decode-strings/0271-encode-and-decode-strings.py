class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encodedString= ""
        for i in strs:
            word_length = str(len(i))
            encodedString += word_length + "\U0001f3ae"+i
        print(encodedString)
        return encodedString
            


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res=[]
        i = 0 
        while i < len(s):
            j=i
            while s[j]!='\U0001f3ae':
              j+=1
            l = int(s[i:j])
            i = j+1
            word=""
            while l>0:
                word +=s[i]
                l-= 1
                i+=1
            res.append(word)
            
        return res




        
       


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
#5!Hello5!World
