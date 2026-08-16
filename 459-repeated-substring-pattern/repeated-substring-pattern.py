class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_fold = "".join( (s[1:], s[:-1]) )
        return s in s_fold
