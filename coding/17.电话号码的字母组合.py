# @lcpr-before-debug-begin
from python3problem17 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        _map={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res=[]
        def backtracking(dighits,tempv):
            if len(dighits)==0:
                if(len(tempv))>0:
                    res.append(tempv)
                return
            v=list(_map[int(dighits[0])])
            for it in v:
                tempv+=it
                backtracking(dighits[1:],tempv)
                tempv=tempv[:-1]
        backtracking(digits,'')
        return res
        
# @lc code=end

