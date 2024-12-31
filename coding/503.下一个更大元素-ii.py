# @lcpr-before-debug-begin
from python3problem503 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mp=[]
        temp = nums[:]
        for it in nums:
            temp.append(it)
        res=[-1]*len(temp)
        for i in range(len(temp)):
            if(len(mp)==0 or temp[i]<=temp[mp[-1]]):
                mp.append(i)
            else:
                while(len(mp)>0 and temp[i]>temp[mp[-1]]):
                    j=mp[-1]
                    mp.pop()
                    res[j]=temp[i]
                mp.append(i)
        return res[:len(nums)]        
# @lc code=end

