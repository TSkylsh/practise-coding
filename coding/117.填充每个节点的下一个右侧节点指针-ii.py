#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import queue
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        res=[]
        if root is None:
            return root
        mq=queue.Queue()
        mq.put(root)
        res.append(root.val)
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
            preNode = None
            if len(temp)>0:
                 for it in temp:
                    if preNode is None:
                        preNode=it
                        preNode.next=None
                    else:
                        preNode.next=it
                        it.next=None
                        preNode=it
        return root
# @lc code=end

