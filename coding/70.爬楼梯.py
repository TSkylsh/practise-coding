#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        nums=[1,2]
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(n+1):
            print(dp)
            for j in range(1,3):
                if i>=nums[j-1]:
                    dp[i]+=dp[i-nums[j-1]]
        print(dp)
        return dp[-1]
        
# @lc code=end

