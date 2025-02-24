#
# @lc app=leetcode.cn id=1035 lang=python3
#
# [1035] 不相交的线
#

# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        text1=nums1
        text2=nums2
        if len(text2)>len(text1):
            text1,text2=text2,text1
        n=len(text1)
        m=len(text2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(text2[i-1]==text1[j-1]):
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])

        return dp[m][n]
# @lc code=end

