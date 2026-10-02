class Solution:
    def convertToBase7(self, num: int) -> str:
        sign=1
        if num<0:
            sign=-1
            num=-1*num
        res=0
        i=0
        while num:
            r=num%7
            res=10**i *r + res
            num=num//7
            i+=1
        return str(res*sign)