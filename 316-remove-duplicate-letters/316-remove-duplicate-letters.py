from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        answer = ''
        stack = []
        for key in s:
            counter[key] -= 1
            if key in stack:
                continue
            while stack and key < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(key)
        return ''.join(stack)
        
       