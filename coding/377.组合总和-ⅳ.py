# @lcpr-before-debug-begin
from python3problem377 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#
#perfect
# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # 初始化 dp 数组
        dp = [[0] * (n + 1) for _ in range(target + 1)]
        # 初始化
        dp[0][0] = 1
        for i in range(0, n + 1):
            dp[0][i]=1
        for i in range(0, target + 1):
            for j in range(1, n + 1):
                if i >= nums[j - 1]:
                    dp[i][j] = dp[i][j - 1] +  + dp[i - nums[j - 1]][-1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[target][n]
# @lc code=end

