class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        max1,max2=float("-inf"),float("-inf")

        while n>0:
            r=n%10
            n=n//10
            if r>= max1:
                max2=max1
                max1=r
            elif r>max2:
                max2=r
        return max1 * max2
