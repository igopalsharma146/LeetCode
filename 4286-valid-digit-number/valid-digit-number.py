class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        s=str(n)
        if int(s[0])==x:
            return False
        for ch in s:
            if  int(ch)==x:
                return True
        return False