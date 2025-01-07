#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res=0
        if root is None:
            return res
        mq=queue.Queue()
        mq.put(root)
        res+=1
        while mq.qsize()>0:
            temp=[]
            _size=mq.qsize()
            for i in range(_size):
                node = mq.get()
                if node.left:
                    temp.append(node.left)
                    mq.put(node.left)
                if node.right:
                    temp.append(node.right)
                    mq.put(node.right)
            if len(temp)>0:
                 res+=1
        return res
# @lc code=end

