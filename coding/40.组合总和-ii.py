#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtracking(candidates,target,temp,l):
            _sum=sum(temp)
            if _sum==target:
                res.append(temp[:])
                return
            elif _sum> target:
                return
            for i in  range(l,len(candidates)):
                v=candidates[i]
                if i>l and candidates[i]==candidates[i-1]:
                    continue
                temp.append(v)
                backtracking(candidates,target,temp,i+1)
                temp.pop()
        backtracking(candidates,target,[],0)
        return res
# @lc code=end

