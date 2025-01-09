#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2==1:
            return False
        target = total//2
        nums.insert(0,0)
        weights = nums
        values = nums
        dp = [0]*(target+1)
        for i in range(1,len(values)):
            for j in range(target,0,-1):
                if j >= weights[i]:
                    dp[j]=max(dp[j-weights[i]]+values[i],dp[j])
        return dp[-1]==target


# @lc code=end

