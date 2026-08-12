# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if root ==None:
            return []

        result=[]
        def path_sum(node,res,currentSum):
            if node.left is None and node.right is None:
                if currentSum == targetSum :
                    result.append(res[:])
                return

            if node.left!=None:
                res.append(node.left.val)
                path_sum(node.left,res,currentSum+node.left.val)
                res.pop()

            if node.right!=None:
                res.append(node.right.val)
                path_sum(node.right,res,currentSum+node.right.val)
                res.pop()

        path_sum(root,[root.val],root.val)
        return result