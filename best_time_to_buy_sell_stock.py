class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		curr_min = prices[0]
		profit = 0
		for i in range(1, len(prices)):
			if prices[i] < curr_min:
				curr_min = prices[i]
			else:
				curr_profit = prices[i] - curr_min
				profit = max(profit, curr_profit)
		return profit



# Steps
# Set profit to 0 (incase we cannot achieve profit)
# Set current minimum to first item in index
# iterate through starting at the second index
# if the next element is less than the previous one, update current minimum

# Else! if it's not, we know we have a profit, so we need to update the profit by...
# take current element and subtract minimum
# see if this profit is larger or smaller than current profit. if larger, update.






# 121. Best Time to Buy and Sell Stock
# Easy

# You are given an array prices where prices[i] is
# the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy
# one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this
# transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#  