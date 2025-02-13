#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        nums=stones
        value=sum(nums)
        _sum=value//2
        dp = [[0]*(_sum+1) for _ in range(0,len(nums))]
        for i in range(nums[0],_sum+1):
            dp[0][i]=nums[0]
        for i in range(1,len(nums)):
            for j in range(1,_sum+1):
                if j>=nums[i]:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-nums[i]]+nums[i])
                else:
                    dp[i][j]=dp[i-1][j]
        return value-2*dp[len(nums)-1][_sum]
# @lc code=end

