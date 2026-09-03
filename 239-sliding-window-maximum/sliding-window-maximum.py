class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        dq = deque()
        for right in range(len(nums)):

            # Remove indices that are outside the window
            while dq and dq[0] < right - k + 1:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)

            # Window has reached size k
            if right >= k - 1:
                res.append(nums[dq[0]])
        return res



        # TLE ERROR
        # res=[]
        # left,right=0,0
        # while right<len(nums):
        #     if (right-left+1)==k:
        #         maxi=float("-inf")
        #         i=left
        #         while i<=right:
        #             maxi=max(maxi,nums[i])
        #             i+=1
        #         res.append(maxi)
        #         left+=1
        #     right+=1
        # return res