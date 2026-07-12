class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        def combinations(index,total,subset):
            if total== target :
                result.append(subset[:])
                return
            if index >= len(candidates) :
                return
            if total > target:
                return
            
            subset.append(candidates[index])
            combinations(index,total + candidates[index],subset)

            subset.pop()
            combinations(index+1,total,subset)
        
        combinations(0,0,[])
        return result
        
