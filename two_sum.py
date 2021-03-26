class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
		n = len(nums)
		for i in range(n):
			for j in range(i+1, n):
				if nums[i] + nums[j] == target:
					return [i, j]


answer = twoSum([3,2,4], 6)
print(answer)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]





#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.


#You can return the answer in any order.