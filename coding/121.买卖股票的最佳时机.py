#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[0]*len(prices) for _ in range(2)]
        dp[0][0]=-prices[0]
        dp[1][0]=0
        for i in range(1,len(prices)):
            dp[0][i]=max(dp[0][i-1],-prices[i])
            dp[1][i]=max(dp[1][i-1],dp[0][i]+prices[i])
        return dp[1][len(prices)-1]
# @lc code=end

