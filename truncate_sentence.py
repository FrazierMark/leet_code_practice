class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
    	s_list = s.split()
    	new_s = []
    	for word in s_list[:k]:
    		new_s.append(word)
    	final_string = ' '.join([str(elem) for elem in new_s])
    	return final_string


       