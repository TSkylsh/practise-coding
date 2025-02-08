# @lcpr-before-debug-begin
from python3problem518 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #
        dp=[[0]*(amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0]=1
        for i in range(coins[0],amount+1):
            dp[0][i]=dp[0][i-coins[0]]

        for i in range(1,len(coins)):
            for j in range(0,amount+1):
                if j>=coins[i] and j-coins[i]>=0:
                    #dp[i][j]=考虑i：dp[i-1][j-nums[i]]*1 + 不考虑i dp[i-1][j]
                    dp[i][j]=dp[i][j-coins[i]]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
# @lc code=end

