#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtracking(candidates,target,temp,i):
            _sum=sum(temp)
            if _sum==target:
                res.append(temp[:])
                return
            elif _sum> target:
                return
            for i in  range(i,len(candidates)):
                v=candidates[i]
                temp.append(v)
                backtracking(candidates,target,temp,i)
                temp.pop()
        backtracking(candidates,target,[],0)
        return res



# @lc code=end

