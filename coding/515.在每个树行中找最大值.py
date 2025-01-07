#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root is None:
            return res
        mq=queue.Queue()
        mq.put(root)
        res.append(root.val)
        while mq.qsize()>0:
            temp=[]
            _size=mq.qsize()
            for i in range(_size):
                node = mq.get()
                if node.left:
                    temp.append(node.left.val)
                    mq.put(node.left)
                if node.right:
                    temp.append(node.right.val)
                    mq.put(node.right)
            if len(temp)>0:
                res.append(max(temp))
        return res
# @lc code=end

