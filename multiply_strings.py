class Solution:
	def multiply(self, num1: str, num2: str) -> str:
		new_num1 = []
		new_num2 = []
		#Convert each number to ascii/unicode Character
		for i in num1:
			i = ord(i) - 48
			new_num1.append(i)

		#Combine array of ints to single int
		strings1 = [str(x) for x in new_num1]
		a_string = "".join(strings1)
		a_integer = int(a_string)
			

		for j in num2:
			j = ord(j) - 48
			new_num2.append(j)

		strings2 = [str(j) for j in new_num2]
		b_string = "".join(strings2)
		b_integer = int(b_string)


		#Multiple ints together and comvert back to string
		result = (a_integer * b_integer)
		result = str(result)
		return  result



multiply("123", "456")

# Given two non-negative integers num1 and num2
#  represented as strings, return the product of
#   num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger
#  library or convert the inputs to integer directly.

 

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"