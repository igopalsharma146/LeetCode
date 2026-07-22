class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num=1
        while num <= n:
            if num == n:
                return True
            num *=4
        return False
            