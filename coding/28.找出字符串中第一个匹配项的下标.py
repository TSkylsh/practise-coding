#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getNext(s1):
            next=[0]*len(s1)
            next[0]=-1
            j=-1
            for i in range(1,len(s1)):
                while(j>=0 and s1[i]!=s1[j+1]):
                    j=next[j]
                if s1[i]==s1[j+1]:
                    j+=1
                next[i]=j
            return next
        next=getNext(needle)
        j=-1
        for i in range(len(haystack)):
            while(j>=0 and haystack[i]!=needle[j+1]):
                j=next[j+]
            if haystack[i]==needle[j+1]:
                j+=1
            if j==(len(needle)-1):
                return i-len(needle)+1
        return -1    
# @lc code=end

