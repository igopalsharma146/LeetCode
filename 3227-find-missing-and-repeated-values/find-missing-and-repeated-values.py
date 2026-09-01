class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        missing=None
        repeated=None
        n=len(grid)
        m=n*n
        s=m*(m+1)/2
        sum1=0
        s1=set()
        for i in range(0,n):
            for j in range(0,n):
                if grid[i][j] in s1:
                    repeated=grid[i][j]
                else:
                    sum1+=grid[i][j]
                    s1.add(grid[i][j])
        return [repeated, s-sum1]