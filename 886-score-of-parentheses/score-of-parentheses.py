class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]   # temp value to help us

        for char in s:
            if char == '(':
                stk.append(0) 
            else:
                value = max(2 * stk.pop(), 1)
                stk[-1] += value
        return stk.pop()