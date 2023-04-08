# Time complexity O(N) 
# Space complexity O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i =='{' or i =='[':
                stack.append(i)

            if i == ')': 
                if not stack or stack.pop() != '(':
                    return False
            if i == ']':
                if not stack or stack.pop() != '[':
                    return False
            if i == '}':
                if not stack or stack.pop() != '{':
                    return False
        if stack:
            return False
        return True

