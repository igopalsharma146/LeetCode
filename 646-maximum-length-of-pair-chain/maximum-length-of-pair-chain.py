class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        count=0
        pairs.sort(key=lambda x:x[1])
        print(pairs)

        stack=[]
        for pair in pairs:
            if not stack or stack[-1][-1] < pair[0]:
                stack.append(pair)
        print(stack)
        return len(stack)