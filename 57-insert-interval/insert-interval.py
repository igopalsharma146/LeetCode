class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        print(intervals)

        stack=[]
        for interval in intervals:
            if not stack or stack[-1][1]<interval[0]:
                stack.append(interval)
            else:
                stack[-1][1]=max(stack[-1][1],interval[1])
        return stack