# @lcpr-before-debug-begin
from python3problem704 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid =(l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r=mid-1
            else:
                l=mid+1
        return -1
# @lc code=end

