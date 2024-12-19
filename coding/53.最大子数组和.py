#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<=0:
            return 0
        cur_sum=nums[0]
        max_sum=cur_sum
        for i in range(1,len(nums)):
            if nums[i]>cur_sum+nums[i]:
                cur_sum=nums[i]
            else:
                cur_sum=cur_sum+nums[i]
            if max_sum<cur_sum:
                max_sum=cur_sum
        return max_sum
            
# @lc code=end

