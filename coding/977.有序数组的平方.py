#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result=[]
        p1=0
        p2=len(nums)-1
        while p1<=p2:
            v1=nums[p1]*nums[p1]
            v2=nums[p2]*nums[p2]
            if v1>v2:
                result.append(v1)
                p1+=1
            else:
                result.append(v2)
                p2-=1
        return result[::-1]

        
# @lc code=end

