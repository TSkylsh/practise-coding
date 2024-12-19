#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=1000002
        res_max=0
        for i in range(0,len(prices)-1):
            price=prices[i]
            _max=prices[i+1]
            for j in range(i+1,len(prices)):
                if prices[j] >_max:
                    _max = prices[j]

            if _max-price > res_max:
                res_max=_max-price
        return res_max
# @lc code=end

