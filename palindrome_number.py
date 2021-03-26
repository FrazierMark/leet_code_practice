class Solution:
	def isPalindrome(self, x: int) -> bool:
	    backwards_string = str(x)[::-1]
	    if x < 0:
	        return False
	    elif int(backwards_string) == x:
	        return True
	    else:
	        return False





isPalindrome(122)

x = 121