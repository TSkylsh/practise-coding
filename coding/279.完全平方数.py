#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[9999999999]*(n+1)
        dp[0]=0
        for i in range(0,n+1):
            for j in range(1,i+1):
                if j*j>i:break
                dp[i]= min(dp[i-j*j]+1,dp[i])
        return dp[-1]


# @lc code=end

