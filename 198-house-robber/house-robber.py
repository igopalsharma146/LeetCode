class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        def solve(index):
            if index==0:
                return nums[index]
            if index<0:
                return 0
            if dp[index]!=-1:
                return dp[index]
            pick=nums[index]+solve(index-2)
            not_pick=0+solve(index-1)
            dp[index]= max(pick,not_pick)
            return dp[index]
        return solve(n-1)