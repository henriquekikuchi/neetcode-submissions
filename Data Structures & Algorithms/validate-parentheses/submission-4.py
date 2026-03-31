class Solution:
    def isValid(self, s: str) -> bool:
        size = len(s)

        if size == 0:
            return True

        if size < 2:
            return False

        p = {
            '[': ']',
            '(': ')',
            '{': '}',
        }

        stack = []

        for k in s:
            if p.get(k) != None:
                stack.append(k)
            elif len(stack) > 0:
                f = stack.pop()
                if p.get(f) == k:
                    continue
                else:
                    return False
            else:
                return False

        if len(stack) > 0:
            return False
        
        return True
