class Solution:
    def sumBase(self, n: int, k: int) -> int:
    	converted_num = []
    	while n is not 0:
    		r = n % k
    		converted_num.insert(0, r)
    		n = n // k

    	return sum(converted_num)



#Steps
#Convert n to base k
	# while n is not 0 ??
	#- n % k = remainder
	#- add remainder to list (beware of what position)
		# converted_num.insert(0, remainder)
	#- n // k = NEW-- n
	#- result is original number in base k
# sum(resulting list)


# Algorithmic example on how to convert base 10 to base 5

# 419 in base 10 to base 5 
# 419 ÷ 5 = 83 r 4, so Base 5 is now: _ _ _ 4.
# 83 ÷ 5 = 16 r 3, so Base 5 is now: _ _ 3 4.
# 16 ÷ 5 = 3 r 1, so Base 5 is now: _ 1 3 4.
# 3 ÷ 5 = 0 r 3, so Base 5 is now: 3 1 3 4.
# So 419 in base 10 is 3134 in base 5.




# 1837. Sum of Digits in Base K
# Easy

# Given an integer n (in base 10) and a base k,
# return the sum of the digits of n
# after converting n from base 10 to base k.
# After converting, each digit should be
# interpreted as a base 10 number,
# and the sum should be returned in base 10.
 
# Example 1:
# Input: n = 34, k = 6
# Output: 9
# Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.

# Example 2:
# Input: n = 10, k = 10
# Output: 1
# Explanation: n is already in base 10. 1 + 0 = 1.


