# @lcpr-before-debug-begin
from python3problem739 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mq=[]
        result=[0]*len(temperatures)
        mq.append(0)
        for i in range(1,len(temperatures)):
            temp=temperatures[i]
            if len(mq)==0 or temperatures[mq[-1]]>=temp:
                mq.append(i)
            else:
                while len(mq)>0 and temperatures[mq[-1]]<temp:
                    j=mq[-1]
                    mq.pop()
                    result[j]=i-j
                mq.append(i)
        return result

# @lc code=end

