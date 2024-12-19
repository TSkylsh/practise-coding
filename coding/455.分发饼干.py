#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g=sorted(g)[::-1]
        s=sorted(s)[::-1]
        i,j=0,0
        count=0
        while i<len(s)and j<len(g):
            if(s[i]>=g[j]):
                i+=1
                j+=1
                count+=1
            else:
                j+=1
        return count



# @lc code=end

