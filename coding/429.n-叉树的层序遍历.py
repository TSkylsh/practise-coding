#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
import queue
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res=[]
        if root is None:
            return res
        mq=queue.Queue()
        mq.put(root)
        res.append([root.val])
        while mq.qsize()>0:
            temp=[]
            _size=mq.qsize()
            for i in range(_size):
                node = mq.get()
                for it in node.children:
                    mq.put(it)
                    temp.append(it.val)
            if len(temp)>0:
                res.append(temp[:])
        return res
                

# @lc code=end

