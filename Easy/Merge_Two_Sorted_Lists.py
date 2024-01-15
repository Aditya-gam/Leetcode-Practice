class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # Check if both lists are empty
        if not list1 and not list2:
            return None
        
        # If one list is empty, return the other list
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Determine the head of the merged list
        head = ListNode()

        # Initialize current pointer
        curr = head

        # Merge the lists
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        # Attach the remaining part of the non-empty list
        curr.next = list1 or list2

        return head.next
