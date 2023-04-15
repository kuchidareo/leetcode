class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(i):
            if i == 0:
                return 0
            elif i < 0:
                return -1

            min_val = float('inf')    
            for coin in coins:
                res = dp(i - coin)
            
                if res != -1:
                    min_val = min(res+1, min_val)

            return min_val if min_val != float('inf') else -1
        
        return dp(amount)
