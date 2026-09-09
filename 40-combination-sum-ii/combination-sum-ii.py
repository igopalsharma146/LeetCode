class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        def combinations(index,total,subset):
            if total== target :
                result.append(subset[:])
                return
            if index >= len(candidates) :
                return
            if total > target:
                return
            
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                combinations(i+1,total+candidates[i],subset+[candidates[i]])
        combinations(0,0,[])
        return result