class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        if n%2 != 0:
            return False
        else:
            stack=[]
            hash_map = {')': '(', ']': '[', '}': '{'}

            for ch in s:
                if ch in hash_map:
                    if stack and stack[-1] == hash_map[ch]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(ch)
        # Return True if stack is empty, False otherwise
        return not stack