class Solution:
    def isValid(self, s: str) -> bool:
        st  = []
        map = {'(':')','{':'}','[':']'}
        for i in s :
            if i in map :
                print(i)
                st.append(i)
            elif len(st) != 0 and map.get(st[-1]) == i :
                st.pop()
            else:
                return False
        return len(st) == 0
                
        
        