class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        current_max = 0
        
        for i in range(len(prices)-1):
            # if the stock we have is the maximum then all the stock,
            # then we will be losing money in that case
            if prices[i] > max(prices[i+1 : ]):
                continue
            else:
                # check what maximum profit we can get, if we sell the current stock
                # from the maximum prices stocks, check for each of the stock 
                max_output = max(prices[i+1: ]) - prices[i]
                if max_output > current_max:
                    current_max = max_output
                    
        return current_max
                
        
