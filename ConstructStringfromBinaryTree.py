# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        #思路：通过递归的方法来解决
        #1.如果t为null，返回" ";
        #2.将每个子节点记为"(" + (string of child) + ")"
        #3.如果存在右子节点但是没有左子节点，需要用"()"而不是空字符串
        if not t:
            return ""
        left, right = '', ''
        if t.left or t.right:
            left = "({})".format(self.tree2str(t.left)) #加上()
        if t.right:
            right = "({})".format(self.tree2str(t.right)) #加上()
        return "{}{}{}".format(t.val, left, right)
