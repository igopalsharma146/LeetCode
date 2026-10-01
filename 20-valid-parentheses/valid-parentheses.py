class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d1={')':'(',']':'[','}':'{'}
        for ch in s:
            if ch not in d1:
                stack.append(ch)
            elif stack and stack[-1]==d1[ch]:
                stack.pop()
            else:
                return False
        print(stack)
        return not stack
