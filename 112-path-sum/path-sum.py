# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False

        def check(node, currentSum):

            # Leaf node
            if node.left is None and node.right is None:
                return currentSum == targetSum

            # Left subtree
            if node.left is not None:
                if check(node.left, currentSum + node.left.val):
                    return True

            # Right subtree
            if node.right is not None:
                if check(node.right, currentSum + node.right.val):
                    return True

            return False

        return check(root, root.val)