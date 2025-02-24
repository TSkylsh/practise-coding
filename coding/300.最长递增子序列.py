# @lcpr-before-debug-begin
from python3problem300 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails=[]
        tails.append(nums[0])
        for it in  nums[1:]:
            l=0
            r=len(tails)
            while l<r:
                mid =(l+r)//2
                if tails[mid]<it:
                    l=mid+1
                else:
                    r=mid
            if l ==len(tails):
                tails.append(it)
            else:
                tails[l]=it
        return len(tails)
            
            

# @lc code=end

