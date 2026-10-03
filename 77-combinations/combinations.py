class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k>n:
            return []
        
        res=[]
        def solve(index,subset):
            if len(subset)==k:
                res.append(subset[:])
                return
            for i in range(index,n+1):
                subset.append(i)
                solve(i+1,subset)
                subset.pop()
        solve(1,[])
        return res