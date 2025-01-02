# @lcpr-before-debug-begin
from python3problem42 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        mp=[]
        temp = height[:]
        mp.append(0)
        res=0
        for i in range(1,len(height)):
            if len(mp)==0 or temp[mp[-1]]>=temp[i]:
                mp.append(i)
            elif temp[mp[-1]]==temp[i]:
                mp.pop()
                mp.append(i)
            else:
                while(len(mp)>0 and temp[mp[-1]]<temp[i]):
                    now=mp[-1]
                    mp.pop()
                    if(len(mp)>0 ):
                        maxh=min(temp[mp[-1]],temp[i])
                        w=i-mp[-1]-1
                        res+=(maxh-temp[now])*w
                mp.append(i)
        return res
                    
# @lc code=end

