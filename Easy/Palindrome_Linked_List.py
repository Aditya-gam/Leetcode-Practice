# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # fast = slow = head
        # curr = head

        # if head is None or head.next is None:
        #     return True
        
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # prev = None
        # while slow:
        #     temp = slow.next
        #     slow.next = prev
        #     prev = slow
        #     slow = temp

        # while prev:
        #     if prev.val != curr.val:
        #         return False
        #     prev = prev.next
        #     curr = curr.next

        # return True

        prev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            prev, prev.next, slow = slow, prev, slow.next

        if fast:
            slow = slow.next

        while prev and prev.val == slow.val:
            slow = slow.next
            prev = prev.next
            
        return not prev
    