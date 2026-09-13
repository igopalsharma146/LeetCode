class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # TLE ERROR
        # n=len(nums)
        # res=[0]*n
        # stack=[]
        # for i in range(n-1,-1,-1):
        #     count=0
        #     stack2=stack[:]
        #     while stack2:
        #         e=stack2.pop()
        #         if e<nums[i]:
        #             count+=1
        #     res[i]=count
        #     stack.append(nums[i])
        # return res

        arr, ans = sorted(nums), []           #  <-- 1)
        for num in nums:
            i = bisect_left(arr,num)          #  <-- 2a)
            ans.append(i)                     #  <-- 2b)
            del arr[i]                        #  <-- 2c)
        return ans  