class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=int(s)
        res=0
        i=0
        while n>0:
            r=n%10
            res += r * 2**i
            i+=1
            n=n//10
        
        ans=0
        while res !=1:
            if res%2 != 0:
                res+=1
                ans+=1
            else:
                res=res//2
                ans+=1
        return ans

        # steps = 0
        # carry = 0
        # n = len(s) - 1
        # for i in range(n, 0, -1):
        #     if int(s[i]) + carry == 1:
        #         carry = 1
        #         steps += 2
        #     else:
        #         steps += 1
        # return steps + carry