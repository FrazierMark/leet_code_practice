class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
    	even = []
    	odd = []
    	for num in nums:
    		if num % 2 == 0:
    			even.append(num)
    		else:
    			odd.append(num)
    	return even + odd



# iterate thorugh array
# if num is even (num % 2 == 0) 
# add to even list
# if not, at to odd list
# join/merge even list and odd list 

# 905. Sort Array By Parity
# Easy

# Given an array nums of non-negative integers, 
# return an array consisting of all the even elements of nums,
# followed by all the odd elements of nums.
# You may return any answer array that satisfies this condition.
 
# Example 1:
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


