# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def sumOfLeft(node):
            if node is None:
                return 0

            total = 0
            if node.left is not None:
                if node.left.left is None and node.left.right is None:
                    total += node.left.val
                else:
                    total += sumOfLeft(node.left)

            total += sumOfLeft(node.right)
            return total

        return sumOfLeft(root)