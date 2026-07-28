class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # Agar k abhi bhi bacha hai to last ke digits remove kar denge.
        while k > 0:
            stack.pop()
            k -= 1

        ans = "".join(stack)
        # Leading zeros remove kar denge
        ans = ans.lstrip("0")
        return ans if ans else "0"

