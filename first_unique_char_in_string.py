class Solution:
	from collections import Counter
	def firstUniqChar(self, s: str) -> int:
		counts = Counter(s)
		for key, value in enumerate(s):
			if counts[value] == 1:
				return key 
            
        return -1
        


# Step
# We will need to keep track of each letter
# and the number of occurances.



# Afterwards we can iterate through dictionary
#  and find letter with 1 occurance. 

#  the first 1 letter occurance will be used to search array again??

        




# Given a string s, find the first non-repeating character 
# in it and return its index. If it does not exist, return -1.



# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
#  