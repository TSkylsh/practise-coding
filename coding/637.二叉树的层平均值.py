#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res=[]
        mq = queue.Queue()
        mq.put(root)
        res.append(root.val/1.0)
        while mq.qsize()>0:
            temp=[]
            length=mq.qsize()
            for i in range(length):
                node = mq.get()
                if node.left:
                    temp.append(node.left.val)
                    mq.put(node.left)
                if node.right:
                    temp.append(node.right.val)
                    mq.put(node.right)
            if len(temp)>0:
                total=sum(temp)
                _len=len(temp)
                res.append(total/_len)
        return res

# @lc code=end

