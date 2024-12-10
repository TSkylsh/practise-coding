# @lcpr-before-debug-begin
from python3problem27 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[p1]=nums[i]
                p1+=1
        return p1



# @lc code=end

