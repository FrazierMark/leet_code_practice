class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_node = ListNode()
        tail = res_node
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
            
        return res_node.next


## for reference - https://www.youtube.com/watch?v=XIdigk956u0 ^^


def mergeTwoLists(l1, l2):
	merged_list = []
	for num in l1:
		merged_list.append(num)
	for num in l2:
		merged_list.append(num)
	sorted_list = sorted(merged_list)
	return(sorted_list)

l1 = [1,2,4]
l2 = [1,3,4]
mergeTwoLists(l1, l2)