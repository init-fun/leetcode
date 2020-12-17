class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        current_max = 0
        for i in range(len(prices)-1):
            if prices[i] > max(prices[i+1 : ]):
                continue
            else:
                max_output = max(prices[i+1: ]) - prices[i] #5
                if max_output > current_max:
                    current_max = max_output #5
                    
        return current_max
                
        
