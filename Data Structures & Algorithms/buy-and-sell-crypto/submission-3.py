class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1
        maxi = 0

        while right < len(prices):
            
            if prices[left] > prices[right]:
                left = right

            elif prices[left] < prices[right]:
                current = prices[right] - prices[left]
                maxi = max(maxi, current)
            
            right += 1

        return maxi

                
        