class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        mini=float("inf")
        maxi=float("-inf")
        sum1=0
        n=len(salary)-2
        for num in salary:
            mini=min(mini,num)
            maxi=max(maxi,num)
            sum1+=num
        print(mini,maxi,sum1,n)
        return float(sum1-mini-maxi)/n