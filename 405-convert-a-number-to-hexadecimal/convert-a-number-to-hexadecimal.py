class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        res=""
        if num==0:
            return "0"
            
        if num<0:
            num=2**32+num
        
        h="0123456789abcdef"
        while num>0:
            r=num%16
            res = h[r] + res
            num=num//16
        return res
        