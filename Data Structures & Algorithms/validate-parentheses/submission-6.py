class Solution:
    def isValid(self, s: str) -> bool:
        reference = {']':'[', ')':'(', '}':'{'}
        stack = []
        for i in range(len(s)):
            if s[i] not in reference:
                stack.append(s[i])
            else:
                if len(stack) == 0 or reference[s[i]] != stack[-1]:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False