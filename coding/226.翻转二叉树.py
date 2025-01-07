#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ms=[]
        if root is None:
            return root
        ms.append(root)
        while len(ms)>0:
            node=ms[-1]
            ms.pop()
            node.left,node.right=node.right,node.left
            if node.left:
                ms.append(node.left)
            if node.right:
                ms.append(node.right)
        return root

        
# @lc code=end

