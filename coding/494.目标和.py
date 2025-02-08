# @lcpr-before-debug-begin
from python3problem494 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #l r l-r=target l+r=sum l-(sum-l)=target l=(target+sum)/2  l=-50sum=-100 r=sum-l=
        #dp[i][j] :考虑[0:i]种物品 价值为J时候 能有多少种组合
        _sum=sum(nums)
        if (target+_sum)%2==1:
            return 0
        l=(target+_sum)//2
        if (abs(target) > _sum) :
            return 0
        dp=[[0]*(l+1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0]=1
        if nums[0]<=l:
            dp[0][nums[0]]+=1

        for i in range(1,len(nums)):
            for j in range(0,l+1):
                if j>=nums[i] and j-nums[i]>=0:
                    #dp[i][j]=考虑i：dp[i-1][j-nums[i]]*1 + 不考虑i dp[i-1][j]
                    dp[i][j]=dp[i-1][j-nums[i]]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
        
        # @lc code=end

