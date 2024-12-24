#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        i=0
        j=len(s)

        def reversePath(s,i,j):
            while(i<j):
                temp=s[i]
                s[i]=s[j]
                s[j]=temp
                i+=1
                j-=1
        while i<j:
            l=i+2*k
            r=min(i+k-1,j-1)
            reversePath(s,i,r)
            i=l
        return ''.join(s)
# @lc code=end

