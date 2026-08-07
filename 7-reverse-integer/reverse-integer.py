class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=1
        if x<0:
            sign=-1
            x=-x

        rev=0
        while x>0:
            r=x%10
            rev=rev*10+r
            x=x//10
        
        if rev <= -2**31 or rev >= 2**31-1 :
            return 0
        else:
            return rev*sign