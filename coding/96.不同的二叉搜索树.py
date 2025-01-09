# @lcpr-before-debug-begin
from python3problem96 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n<=3:
            dp=[0]*(4)
        else:
            dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            for j in range(0,i):
                dp[i]+=dp[j]*dp[i-j-1]
        return dp[n]
# @lc code=end

