class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        arr=[]
        for word in words:
            l=[]
            for j in range(1,len(word)):
                diff=ord(word[j])-ord(word[j-1])
                l.append(diff)
            arr.append(l)
        
        for i in range(1,len(arr)-1):
            if arr[i]!=arr[i-1] and arr[i]!=arr[i+1]:
                return words[i]
            elif arr[i]!=arr[i-1] and arr[i]==arr[i+1]:
                return words[i-1]
        return words[i+1]

