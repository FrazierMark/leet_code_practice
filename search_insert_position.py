class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		for index,value in enumerate(nums):
			if value == target:
				return index
			elif value > target:
				return index
			# If last element is less than target, return last index
			elif nums[-1] < target:
				return len(nums)




#steps
# Search array for target,
# if found return index,
# if value is larger than target just return that index
# 

# Return index 



# Search Insert Position


# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4