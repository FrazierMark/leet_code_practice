class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # convert list of ints to string
        int_num = ''.join(str(e) for e in num)
        summed = int(int_num) + k
        stringged_sum = str(summed)
        final_string = []
        for ele in stringged_sum:
        	final_string.append(ele)
        return final_string
