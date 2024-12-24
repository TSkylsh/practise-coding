#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        inputs=s.split(' ')
        i=0
        j=len(inputs)-1
        while(i<j):
            temp=inputs[i]
            inputs[i]=inputs[j]
            inputs[j]=temp
            i+=1
            j-=1
        res=''
        for item in inputs:
            if item==' ':
                continue
            res+=item
            res+=' '
        return res[:-1]
# @lc code=end

