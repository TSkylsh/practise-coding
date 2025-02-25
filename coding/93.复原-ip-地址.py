# @lcpr-before-debug-begin
from python3problem93 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def check(substr):
            # 如果子串以 0 开头且长度大于 1，不是有效的 IP 段
            if substr[0] == '0' and len(substr) > 1:
                return False
            # 如果子串转换为整数后不在 0 到 255 范围内，不是有效的 IP 段
            if int(substr) > 255 or int(substr) < 0:
                return False
            return True

        def backtracking(s, startIndex, temp, deep):
            # 当分割出 4 段且刚好遍历完字符串时，说明找到了一个有效的 IP 地址
            if deep == 4:
                if startIndex == len(s):
                    # 将列表中的元素用点号连接成字符串
                    res.append('.'.join(temp))
                return
            # 遍历从 startIndex 开始的所有可能的子串
            for i in range(startIndex, min(startIndex + 3, len(s))):
                _s = s[startIndex:i + 1]
                if check(_s):
                    temp.append(_s)
                    # 递归调用，从 i + 1 开始继续分割
                    backtracking(s, i + 1, temp, deep + 1)
                    # 回溯操作，移除最后添加的元素
                    temp.pop()

        backtracking(s, 0, [], 0)
        return res



# @lc code=end

