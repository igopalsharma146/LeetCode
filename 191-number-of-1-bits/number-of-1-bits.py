class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary=0
        while(n>0):
            bit=n%2
            binary=binary*10+bit
            n=n//2
        binarystring=str(binary)
        count=0
        for i in binarystring:
            if(int(i)==1):
                count+=1
        return count
