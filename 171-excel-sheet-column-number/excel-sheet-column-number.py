class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        output=0
        j=1
        for i in range(1,len(columnTitle)+1):
            if i==1:
                output+=ord(columnTitle[-i])-64
            else:
                output+=(ord(columnTitle[-i])-64)*26**j
                j+=1
        return output