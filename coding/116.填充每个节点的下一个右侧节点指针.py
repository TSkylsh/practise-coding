#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
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

