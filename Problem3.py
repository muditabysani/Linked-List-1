# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def detectCycle(self, head):
		slow = fast = head
		while fast != None and fast.next != None:
			slow = slow.next
			fast = fast.next.next
			if fast == slow:
				while head != slow:
					head = head.next
					slow = slow.next
				return slow
		return None