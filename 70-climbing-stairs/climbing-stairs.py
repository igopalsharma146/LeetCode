class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #edge cases
        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
        dp = [0]*(n+1) # considering zero steps we need n+1 places
        dp[1]= 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] +dp[i-2]
        print(dp)
        return dp[n]
		

        # memo ={}
        # memo[1] = 1
        # memo[2] = 2
        
        # def climb(n):
        #     if n in memo: # if the recurssion already done before first take a look-up in the look-up table
        #         return memo[n]
        #     else:   # Store the recurssion function in the look-up table and reuturn the stored look-up table function
        #         memo[n] =  climb(n-1) + climb(n-2)
        #         return memo[n]
        
        # return climb(n)