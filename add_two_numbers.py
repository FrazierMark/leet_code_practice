
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # create a final-added node, adding together first values
        # if greater than 9, 1 will be stored in the node
        # % 10 make sure we are not storing anything over 9
        added = ListNode(val = (l1.val + l2.val) % 10)

        # floor divide 10, if less than 10 it will return 0
        # if greater than 10 it will return 1
        carry_over = (l1.val + l2.val) // 10

        current_node = added

        # Continues the above calculation as long as both linked_list
        # don't end...
        while(l1.next and l2.next):

        	# go to next nodes
        	l1 = l1.next
        	l2 = l2.next

        	# add another node to our added link_list (added)
        	current_node.next = ListNode(val = (carry_over + l1.val + l2.val) % 10)
        	carry_over = (carry_over + l1.val + l2.val) // 10

        	#updates current node to this newly made node
        	current_node = current_node.next


        # edge cases: if l1 or l2 ends before the other,
        # we need to continue calculating 
        while(l1.next):
        	l1 = l1.next
        	current_node.next = ListNode(val = (carry_over + l1.val) % 10)
        	carry_over = (carry_over + l1.val) // 10
        	current_node = current_node.next

        while(l2.next):
        	l2 = l2.next
        	current_node.next = ListNode(val = (carry_over + l2.val) % 10)
        	carry_over = (carry_over + l2.val) // 10
        	current_node = current_node.next

        # if we have an extra 1 at the end, we need to account for that
        if carry_over > 0:
        	current_node.next = ListNode(val = 1)


        return added





# Add Two Numbers
# Medium

# You are given two non-empty linked lists representing
# two non-negative integers. The digits are stored in
# reverse order, and each of their nodes contains a single digit.
#  Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any
#  leading zero, except the number 0 itself.


# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Still new to nodes and linked lists
# most of this is from...
# https://www.youtube.com/watch?v=IkuWJSYqFAw