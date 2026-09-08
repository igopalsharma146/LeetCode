class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxi = 0
        for i in range(1,len(nums)):
           maxi = max(maxi, (nums[i]-nums[i-1]))
        return maxi


        # if len(nums)<2:
        #     return 0
        # # Merge Sort
        # def merge(left,right):
        #     res=[]
        #     m,n=len(left),len(right)
        #     i,j=0,0
        #     while i<m and j<n:
        #         if left[i]<right[j]:
        #             res.append(left[i])
        #             i+=1
        #         else:
        #             res.append(right[j])
        #             j+=1
        #     while i<m:
        #         res.append(left[i])
        #         i+=1
        #     while j<n:
        #         res.append(right[j])
        #         j+=1
        #     return res
        # def partition(arr):
        #     if len(arr)<=1:
        #         return arr
        #     mid=len(arr)//2
        #     left=partition(arr[:mid])
        #     right=partition(arr[mid:])
        #     return merge(left,right)
        # nums=partition(nums)
        # # print(nums)

        # maxi=0
        # left,right=0,1
        # while right<len(nums):
        #     maxi=max(maxi,nums[right]-nums[left])
        #     left+=1
        #     right+=1
        # return maxi