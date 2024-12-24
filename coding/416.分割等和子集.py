#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        value=sum(nums)
        _sum=value//2
        if value%2==1:
            return False
        dp = [[0]*(_sum+1) for _ in range(0,len(nums))]
        for i in range(nums[0],_sum+1):
            dp[0][i]=nums[0]
        for i in range(1,len(nums)):
            for j in range(1,_sum+1):
                if j>=nums[i]:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-nums[i]]+nums[i])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[len(nums)-1][_sum]==_sum

# @lc code=end

