class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        s1=preorder.split(",")
        degree = 1
        
        for node in s1:
            degree -= 1
            
            if degree < 0: 
                return False
            
            if node != '#': 
                degree += 2 
        return degree == 0