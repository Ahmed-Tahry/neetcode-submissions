class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best_prof = 0
        curr_pos = 0
        for i in range(1,len(prices)):
            j=i
            k=j
            curr_prof = 0
            while curr_prof >=0 and j < len(prices) :
                curr_prof = prices[j]-prices[curr_pos]
                if curr_prof >= best_prof:
                    best_prof = curr_prof
                j = j+1
            curr_pos = curr_pos +1
        
        return best_prof