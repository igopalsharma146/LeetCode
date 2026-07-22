class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n & (n - 1)) == 0 and n % 3 == 1

        # num=1
        # while num <= n:
        #     if num == n:
        #         return True
        #     num *=4
        # return False

        
            