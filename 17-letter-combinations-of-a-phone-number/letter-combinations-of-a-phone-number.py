class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        hash1={
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }
        result=[]
        def backtrack(idx , curr_state):
            if idx == len(digits):
                result.append(curr_state)
                return 
            
            for i in hash1[digits[idx]]:
                backtrack(idx+1, curr_state+i)

        backtrack(0,"")
        return result