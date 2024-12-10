#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1=0
        res=len(nums)+1
        length=0
        sum=0
        for i in range(0,len(nums)):
            sum+=nums[i]
            length+=1
            while(sum>=target):
                if res>length:
                    res=length
                sum-=nums[p1]
                p1+=1
                length-=1
        if(res==len(nums)+1):
            return 0
        return res



        
# @lc code=end

