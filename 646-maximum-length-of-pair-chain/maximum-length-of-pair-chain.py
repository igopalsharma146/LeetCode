class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        cur, ans = float('-inf'), 0
        
        for pair in pairs:
            if cur < pair[0]:
                cur = pair[1]
                ans += 1      
        return ans


        # pairs.sort(key=lambda x:x[1])
        # print(pairs)

        # stack=[]
        # for pair in pairs:
        #     if not stack or stack[-1][-1] < pair[0]:
        #         stack.append(pair)
        # print(stack)
        # return len(stack)