class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        def int_to_bin(n):
            binary=0
            i=0
            while(n>0):
                bit=n%2
                binary=binary+bit*10**i
                n=n//2
                i+=1
            return binary

        num=int_to_bin(n)
        res=str(num)
        return res.count('1')
