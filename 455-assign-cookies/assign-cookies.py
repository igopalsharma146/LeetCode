class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count=0
        g.sort()
        s.sort()
        left,right=0,0
        while left<len(g) and right<len(s):
            if s[right] >= g[left]:
                count+=1
                left+=1
            right+=1
        return count