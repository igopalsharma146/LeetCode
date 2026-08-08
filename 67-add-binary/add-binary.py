class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def bin_to_int(n):
            num=int(n)
            res=0
            i=0
            while num>0:
                r=num%10
                res=res+r*2**i
                num=num//10
                i+=1
            return res

        def int_to_bin(num):
            res=0
            i=0
            while num>0:
                r=num%2
                res=res+r*10**i
                num=num//2
                i+=1
            return str(res)
        num1=bin_to_int(a)
        num2=bin_to_int(b)
        res=int_to_bin(num1+num2)
        return res
