#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #l r l-r=target l+r=sum l-(sum-l)=target l=(target+sum)/2
        _sum=sum(nums)
        if (target+_sum)%2==1:
            return 0
        l=(target+_sum)//2
        
        dp=[[0]*(l+1) for _ in range()]

        return l
        
# @lc code=end

