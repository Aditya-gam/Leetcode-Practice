class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Edge case: Empty list
        if not head:
            return False

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Cycle detected
            if slow == fast:
                return True
            
        # No cycle found
        return False
