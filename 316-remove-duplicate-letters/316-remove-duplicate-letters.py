from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        diction, stack = Counter(s), []
        for tmp in s:
            diction[tmp] -= 1
            if tmp in stack:
                continue
            while stack and tmp < stack[-1] and diction[stack[-1]] > 0:
                stack.pop()
            stack.append(tmp)
        return ''.join(stack)