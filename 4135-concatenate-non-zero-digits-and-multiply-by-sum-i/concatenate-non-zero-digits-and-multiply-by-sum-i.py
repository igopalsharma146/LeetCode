class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum1=0
        ans=0
        s=str(n)
        for ch in s:
            if ch != "0":
                sum1 += int(ch)
                ans= ans*10 + int(ch)
        return ans*sum1