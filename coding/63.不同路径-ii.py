#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp= [[0]*n for _ in range(0,m)]
        if obstacleGrid[0][0]==1:
            return 0 
        dp[0][0]=1
        for i in range(1,n):
            if(obstacleGrid[0][i]==1):
                dp[0][i]=0
            else:
                dp[0][i]=dp[0][i-1]
        for j in range(1,m):
            if(obstacleGrid[j][0]==1):
                dp[j][0]=0
            else:
                dp[j][0]=dp[j-1][0]
        for i in range(1,m):
            for j in range(1,n):
                if(obstacleGrid[i][j]==1):
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
# @lc code=end

