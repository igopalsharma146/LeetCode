class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum1=0
        prod=1
        num=n
        while num>0:
            rem=num%10
            sum1+=rem
            prod*=rem
            num=num//10
        if n%(sum1+prod)==0:
            return True
        else:
            return False