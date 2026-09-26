class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        prefix = [1] * n
        suffix = [1] * n
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        answer = [prefix[i] * suffix[i] for i in range(n)]
        return answer


        # output = [1] * len(nums)

        # left = 1
        # for i in range(len(nums)):
        #     output[i] *= left
        #     left *= nums[i]

        # right = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     output[i] *= right
        #     right *= nums[i]
        # return output 