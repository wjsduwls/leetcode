class Solution:
    def isValid(self, s: str) -> bool:
        diction = {'(':')','{':'}','[':']'}
        s = list(s)
        tmp = []
        while len(s):
            element = s.pop(0)
            if element in diction:
                tmp.append(element)
            else:
                if len(tmp) == 0:
                    return False
                else:
                    if diction[tmp[-1]] == element:
                        tmp.pop()
                    else:
                        return False
        if len(tmp) == 0:
            return True
        return False