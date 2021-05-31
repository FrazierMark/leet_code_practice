class Solution:
	def sumOfUnique(self, nums: List[int]) -> int:
		total = 0
		for num in nums:
		#if duplicate num is not in nums add num to total
			if nums.count(num) == 1:
				total += num
		return total




# class Solution:
# 	def sumOfUnique(self, nums: List[int]) -> int:
# 		unique_nums = []
# 		for num in nums:
# 			if num not in unique_nums:
# 				unique_nums.append(num)
# 			else:
# 				unique_nums.remove(num)
# 		if unique_nums:
# 			return sum(unique_nums)
# 		else:
# 			return 0




sumOfUnique([1,2,3,2])


# iterate through
# 
# count the number of times number appears in list,
# if it appears once, add it to the total

# 1748. Sum of Unique Elements
# Easy


# You are given an integer array nums.
# The unique elements of an array are the elements
# that appear exactly once in the array.
# Return the sum of all the unique elements of nums.
 
# Example 1:
# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.

# Example 3:
# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
 

        
