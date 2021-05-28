class Solution:
	def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
		largest_int = max(candies)
		list_bool = []
		for num in candies:
			if num + extraCandies >= largest_int:
				list_bool.append(True)
			else:
				list_bool.append(False)
		return list_bool


#Steps
# find largest int in the array
# set a variable === to that

# if extra candies PLUS the candies[i]
# is greater that extraCandies:...

# then we want to output true
# else output false




# Example
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 



# Given the array candies and the integer extraCandies,
# where candies[i] represents the number of candies
# that the ith kid has.

# For each kid check if there is a way to distribute
# extraCandies among the kids such that he or she can
# have the greatest number of candies among them.
# Notice that multiple kids can have the greatest

