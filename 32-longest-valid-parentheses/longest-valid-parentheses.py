class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        l=['0']*len(s)
        for ind,i in enumerate(s):
            if i=='(':
                stack.append(ind)
            else:
                if stack:
                    l[stack.pop()]='1'
                    l[ind]='1'
        return max(len(i) for i in ''.join(l).split('0'))

        # # Another solution
        # max_length = 0
                
        # l,r=0,0        
        # # traverse the string from left to right
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         l+=1
        #     else:
        #         r+=1                        
        #     if l == r:# valid balanced parantheses substring 
        #         max_length=max(max_length, l*2)
        #     elif r>l: # invalid case as ')' is more
        #         l=r=0
        
        # l,r=0,0        
        # # traverse the string from right to left
        # for i in range(len(s)-1,-1,-1):
        #     if s[i] == '(':
        #         l+=1
        #     else:
        #         r+=1            
        #     if l == r:# valid balanced parantheses substring 
        #         max_length=max(max_length, l*2)
        #     elif l>r: # invalid case as '(' is more
        #         l=r=0
        # return max_length