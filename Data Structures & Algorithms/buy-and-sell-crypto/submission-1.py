class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices_len = len(prices)
        if prices_len < 1:
            return 0

        response = 0
        remain_max_price = max(prices)
        for idx, price in enumerate(prices[0:]):
            if remain_max_price == price and idx + 1 < prices_len:
                remain_max_price = max(prices[idx + 1:])
            
            profit = remain_max_price - price 
            if profit > response:
                response = profit

        return response
            
