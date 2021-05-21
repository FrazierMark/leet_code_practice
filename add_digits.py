class Solution:
	def addDigits(self, num: int) -> int:
		if num == 0:
			return 0
		if num % 9 == 0:
			return 9
		return (num % 9)


# explained : https://www.youtube.com/watch?v=YJpVLSgLe0w

# pattern 0 -> 9
# 1-> 1
# 2-> 2
# 3-> 3
# 4-> 4
# 5-> 5
# 6-> 6
# 7-> 7
# 8-> 8
# 9-> 9<<<<<<<<


# 10-> 1
# 11-> 2
# 12-> 3
# 13-> 4
# 14-> 5
# 15-> 6
# 16-> 7
# 17-> 8
# 18-> 9<<<<<<

# 19-> 10-> 1
# 20-> 2
# 21-> 3
# 22-> 4
# 23-> 5
# 24-> 6
# 25-> 7
# 26-> 8
# 27-> 9 <<<<<<
# 28-> 10-> 1

# 29-> 11-> 2
# 30-> 3
# 31-> 4
# 32-> 5
# 33-> 6
# 34-> 7
# 35-> 8
# 36-> 9 <<<<
# 37-> 10-> 1
# 38-> 11-> 2

# 39742 -> added up -> 25 -> added up -> 7 <<<<<<<<<<<<<<<<<<<<<<<<
# 39742 % 9 -> 7

# KEY , %9 ALWAYS returns the added digits


# Given an integer num, repeatedly add all its digits
# until the result has only one digit, and return it.

