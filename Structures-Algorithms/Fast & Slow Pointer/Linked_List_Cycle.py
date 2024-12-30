# Leetcode 141, linked list cycle, given the head determine if there is a linked list cycle
head = [3, 2, 0, -4]
pos = 1
print(head)
 # put each node we visit in a hashset in if there is a cycle we will visit the nodes multiple times
 # because of this the mem: O(n) because we can visit each node once and the T: O(n)

class Solution:
    def  hasCycle(self, head: Listnode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next # move one node
            fast = fast.next.next # move two nodes
            if slow == fast:
                return True
            return False
# fast and slow pointers will always meet each other if there is a cycle