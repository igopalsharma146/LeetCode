class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n==1 or n==7):
            return True
        elif(n<10):
            return False
        else:
            sum =0
            while(n>0):
                temp = n%10
                sum += temp*temp
                n= n//10
            return self.isHappy(sum) 

        # hset = set()
        # while n != 1:
        #     if n in hset: return False
        #     hset.add(n)
        #     n = sum([int(i) ** 2 for i in str(n)])
        # else:
        #     return True