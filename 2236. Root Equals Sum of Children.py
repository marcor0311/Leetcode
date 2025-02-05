# Imperative solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.left and root.right:
            left_node = root.left.val
            right_node = root.right.val
            if left_node + right_node == root.val:
                return True
            else:
                return False
        return False
    
# Recursive solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False

        if root.left is None and root.right is None:
            return False

        if root.left and root.right:
            left_node = root.left.val
            right_node = root.right.val

            # Remember this returns a boolean value
            return left_node + right_node == root.val
        
        return False
    
# Simplified recursive solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return root.left.val + root.right.val == root.val