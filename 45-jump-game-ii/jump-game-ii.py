class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # left,right=0,0
        # jump=0
        # while right<len(nums)-1:
        #     farthest=0
        #     for i in range(left,right+1):
        #         farthest=max(farthest,i+nums[i])
        #     left=right+1
        #     right=farthest
        #     jump+=1
        # return jump

        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            # Update the farthest index we can reach
            if i + nums[i] > farthest:
                farthest = i + nums[i]

            # If we reach the end of the current jump
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps