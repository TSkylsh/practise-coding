# @lcpr-before-debug-begin
from python3problem474 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start dp[m][n]
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        for it in strs:
            _str=list(it)
            zeronums=0
            onenums=0
            for i in range(len(_str)):
                if _str[i]=='0':
                    zeronums+=1
                else:
                    onenums+=1
            for i in range(m,zeronums-1,-1):
                for j in range(n,onenums-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-zeronums][j-onenums]+1)
        return dp[-1][-1]
# @lc code=end

