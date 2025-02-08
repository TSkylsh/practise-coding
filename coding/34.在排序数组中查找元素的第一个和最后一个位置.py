# @lcpr-before-debug-begin
from python3problem34 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
    
# @lc code=start
 class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        while l<=r:
            mid =(l+r)//2
            if nums[mid] == target:
                l=mid
                break
            elif nums[mid] > target:
                r=mid-1
            else:
                l=mid+1
        if l<0 or l>=len(nums) or nums[l]!=target :
            return[-1,-1]
        else:
            maxindex,minindex=l,l
        while(minindex-1>=0):
            if(nums[minindex-1]==target):
                minindex-=1
            else:
                break
        while(maxindex+1<len(nums)):
            if(nums[maxindex+1]==target):
                maxindex+=1
            else:
                break
        return [minindex,maxindex]
# @lc code=end

