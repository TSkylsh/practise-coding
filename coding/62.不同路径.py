#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[0]*n for _ in range(0,m)]
        for i in range(0,n):
            dp[0][i]=1
        for j in range(0,m):
            dp[j][0]=1
            for i in range(1,n):
                for j in range(1,m):
                    dp[j][i]=dp[j-1][i]+dp[j][i-1]
        return dp[m-1][n-1]
# @lc code=end

