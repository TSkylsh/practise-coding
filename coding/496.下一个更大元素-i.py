#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp=[]
        m_map={}
        temp=nums2[:]
        res=[-1]*len(temp)
        res1=[]
        for i in range(len(temp)):
            m_map[temp[i]]=i
            if(len(mp)==0 or temp[i]<=temp[mp[-1]]):
                mp.append(i)
            else:
                while(len(mp)>0 and temp[i]>temp[mp[-1]]):
                    j=mp[-1]
                    mp.pop()
                    res[j]=temp[i]
                mp.append(i)
        for it in nums1:
            res1.append(res[m_map[it]])
        return res1
# @lc code=end

