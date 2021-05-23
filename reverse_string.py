class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(len(s)):		# Loop once for every item in list
        	s.insert(i, s.pop())	# remove last element and place in reversed index.

        

# could also do>>>>>>> s.reverse() 


# Write a function that reverses a string.
# The input string is given as an array of characters s.

# Example:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

