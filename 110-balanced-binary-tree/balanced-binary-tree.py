# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def height(node):

            if node is None:
                return 0

            leftHeight = height(node.left)

            # Agar left subtree already unbalanced hai
            if leftHeight == -1:
                return -1

            rightHeight = height(node.right)

            # Agar right subtree already unbalanced hai
            if rightHeight == -1:
                return -1

            # Current node par balance check
            if abs(leftHeight - rightHeight) > 1:
                return -1

            # Current subtree ki height
            return 1 + max(leftHeight, rightHeight)

        return height(root) != -1
        