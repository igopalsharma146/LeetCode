class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            str1=str(n)
            prod=1
            while str1:
                prod*=int(str1[0])
                str1=str1[1:]
            if prod%t==0:
                return n
            n=n+1