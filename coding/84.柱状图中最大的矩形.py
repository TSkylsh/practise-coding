#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        dp=[[0]*len(heights) for _ in range(2)]
        dp[0][0]=-1
        for i in range(1,len(heights)):
            t=i-1
            while(t>0 and heights[i]<=heights[t]):
                t=dp[0][t]
            dp[0][i]=t
        
        dp[1][len(heights)-1]=len(heights)
        for i in range(len(heights)-2,-1,-1):
            t=i+1
            while(t<len(heights) and heights[i]<=heights[t]):
                t=dp[1][t]
            dp[1][i]=t
        res=0
        for i in range(len(heights)):
            res=max(res,heights[i]*( dp[1][i]-dp[0][i]-1))
        return res
# @lc code=end

