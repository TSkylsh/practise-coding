# @lcpr-before-debug-begin
from python3problem102 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if root is  None:
            return res
        mq=queue.Queue()
        mq.put(root)
        res.append([root.val])
        while(mq.qsize()>0):
            temp=[]
            mq_size=mq.qsize()
            for i in range(mq_size):
                node=mq.get()
                if node.left is not None:
                    temp.append(node.left.val)
                    mq.put(node.left)
                if node.right is not None:
                    temp.append(node.right.val)
                    mq.put(node.right)
            if len(temp)>0:
                res.append(temp[:])
        return res


# @lc code=end

