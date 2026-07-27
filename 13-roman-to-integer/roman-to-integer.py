class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d1={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        n=len(s)
        res=0
        for i in range(0,n):
            if i<(n-1) and d1[s[i]] < d1[s[i+1]]:
                res -= d1[s[i]]
            else:
                res += d1[s[i]]
        return res