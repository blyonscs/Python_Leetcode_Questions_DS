#Leetcode 21 Merge Two Sorted Lists, Merge two sorted lists into a new sorted list
l1 = [1, 2, 4], l2 = [1, 3, 4] # input 1 -> 2 -> 4, 1 -> 3 -> 4, output 1 -> 1 -> 2 -> 3 -> 4 -> 4


class Solution:
    def  mergeSorted(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

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
        
        return dummy.next
    