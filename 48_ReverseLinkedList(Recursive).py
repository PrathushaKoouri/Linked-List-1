# accepted in leetcode
# time - O(N), space - O(N), SpacePhysically - O(1)
# draw the recursive stack and put the logic to understand it better.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        l = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return l