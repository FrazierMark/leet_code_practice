class Solution:
    def isValid(self, s: str) -> bool:
    	stack = []
    	info_dict = {")": "(", "}": "{", "]": "["}
    	
    	for symbol in s:
    		if symbol in info_dict.keys():
    			if stack:
    				top_elem = stack.pop()
    			else:
    				top_elem = "gar"
    			
    			if info_dict[symbol] != top_elem:
    				return False
    		else:
    			stack.append(symbol)
    	return not stack


    	

        





