# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        unique = set()
        prev = None
        curr = head
        while curr:
            if curr.val in unique:
                prev.next = curr.next
            else:
                unique.add(curr.val)
                prev = curr
            curr = curr.next

        return head

            