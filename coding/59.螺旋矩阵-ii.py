# @lcpr-before-debug-begin
from python3problem59 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        loop = n//2
        res = [[0]*n for _ in range(0,n)]
        startx=0
        starty=0
        offset=1
        val=1
        while loop:
            for i in range(startx,n-offset):
                res[starty][i]=val
                val+=1
            for j in range(starty,n-offset):
                res[j][n-offset]=val
                val+=1
            for i in range(n-offset,startx,-1):
                res[n-offset][i]=val
                val+=1
            for j in range(n-offset,starty,-1):
                res[j][startx]=val
                val+=1
            startx+=1
            starty+=1
            offset+=1
            loop-=1
        if n%2==1:
            res[n//2][n//2]=n*n

        return res

            
        
# @lc code=end

