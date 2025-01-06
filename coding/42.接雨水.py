# @lcpr-before-debug-begin
from python3problem42 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        mq=[]
        mq.append(0)
        res = 0
        for i in range(1,len(height)):
            if len(mq)==0 or height[mq[-1]]>height[i]:
                mq.append(i)
            elif height[mq[-1]]==height[i]:
                mq.append(i)
            else:
                while len(mq)>0 and height[mq[-1]]<=height[i]:
                    mid=mq[-1]
                    hmid=height[mid]
                    mq.pop()
                    if len(mq)>0:
                        h=min(height[mq[-1]],height[i])-hmid
                        w=i-mq[-1]-1
                        res+=h*w
                mq.append(i)
        return res
                    
# @lc code=end

