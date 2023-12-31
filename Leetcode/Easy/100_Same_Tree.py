# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        result_p = []
        result_q = []
        def solution(tree, result):
            if tree is None:
                result.append(None)
                return
            result.append(tree.val)
            solution(tree.left, result)
            solution(tree.right, result)

        solution(p, result_p)
        solution(q, result_q)
        return result_p == result_q