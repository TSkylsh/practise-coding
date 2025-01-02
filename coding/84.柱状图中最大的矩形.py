#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mp=[]
        temp=heights[:]
        temp=list(reversed(temp))
        temp.append(0)
        temp=list(reversed(temp))
        temp.append(1)
        print(temp)
# @lc code=end

