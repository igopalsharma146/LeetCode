class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def backtrack(openCount, closeCount, subset):

            if openCount == n and closeCount == n:
                result.append("".join(subset))
                return

            if openCount < n:
                subset.append("(")
                backtrack(openCount + 1, closeCount, subset)
                subset.pop()

            if closeCount < openCount:
                subset.append(")")
                backtrack(openCount, closeCount + 1, subset)
                subset.pop()

        backtrack(0, 0, [])
        return result