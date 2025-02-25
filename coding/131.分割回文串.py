# @lcpr-before-debug-begin
from python3problem131 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def check(s):
            return s==s[::-1]
        def backtracking(s,index,temp):  
            if index>=len(s):
                res.append(temp[:])  
                return
            for i in range(index,len(s)):
                v=s[index:i+1]
                if(check(v)):
                    temp.append(v)
                    backtracking(s,i+1,temp)
                    temp.pop()
        backtracking(s,0,[])
        return res
# @lc code=end

