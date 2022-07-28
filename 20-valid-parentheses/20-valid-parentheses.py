class Solution:
    def isValid(self, s: str) -> bool:
        str_dict = {'}':'{', ')':'(', ']':'['}
        s = list(s)
        stack = []
        while len(s):
            char = s.pop(0)
            if char in str_dict:
                if stack and str_dict[char] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        return False
            