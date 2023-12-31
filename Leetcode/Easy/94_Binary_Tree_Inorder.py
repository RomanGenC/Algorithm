# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lis = []
        def solution(tree):
            if tree is None:
                return
            solution(tree.left)
            lis.append(tree.val)
            solution(tree.right)
        solution(root)
        return lis