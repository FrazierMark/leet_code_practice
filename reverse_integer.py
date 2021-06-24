class Solution:
    def reverse(self, x: int) -> int:
        stringed_int = str(x)
        int_array = [x for x in stringed_int]
        int_array.reverse()
        if int_array[-1] == "-":
            int_array.insert(0, "-")
            int_array.pop()
        flipped_string = int("".join(int_array))
        if int(flipped_string) < -2**31 or int(flipped_string) > 2**31-1:
            return 0
        else:
            return flipped_string



# Clean solution using slicing vs mine (above)
def reverse(self, x: int) -> int:
    if x==0:
        return x
    if x > 0:
        rev = int(str(x)[::-1])
    else:
        rev = int(f'-{str(x)[1:][::-1]}')

    if rev > 2147483648 or rev < -2147483648:
        return 0
    return rev



#Steps
# reverse number
    # convert int to string and then to array
    # reverse(array)
    # convert back to int

# if number is greater than... or less than ... then return 0 
# else return reveresed



# Given a signed 32-bit integer x, return x with its
# digits reversed. If reversing x causes the value
# to go outside the signed 32-bit integer
# range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you
# to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
