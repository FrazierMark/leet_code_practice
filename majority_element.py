
class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		frequency = 0
		max_num = 0
		for num in nums:
			if nums.count(num) <= frequency:
				continue 
			else:
				nums.count(num) >= frequency:
				frequency = nums.count(num)
				max_num = num
		return max_num


# Times out-^^
# Works-vv

 
class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		nums.sort()
		# returns element at center index
		# middle element guarenteed to be the majority element
		return nums[len(nums)//2]


def majorityElement(nums):
	nums.sort()
	print(nums)
	# returns element at center index
	# middle element guarenteed to be the majority element
	print (nums[len(nums)//2])




majorityElement([6,5,5])


#Steps
# - count number of times element appears in array
# - if number is larger than max_num
# - set number has new max_num


# 169. Majority Element


# Given an array nums of size n, return the majority element.

# The majority element is the element that appears
# more than ⌊n / 2⌋ times. You may assume that the
# majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3


# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#  