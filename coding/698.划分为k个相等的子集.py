# @lcpr-before-debug-begin
from python3problem698 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        _sum=sum(nums)
        if _sum%k!=0:
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
        g=_sum//k
        i=g 
        j=1
        n=len(nums)
        while(i<=_sum):
            if(dp[n-1][i]!=j*g):
               return False
            j+=1
            i=g*j
        return True
        
# @lc code=end

