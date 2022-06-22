'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        l3 = ListNode()
        l3_head = l3
        while list1 and list2:
            if list1.val < list2.val:
                l3.next = ListNode(list1.val)
                list1, l3 = list1.next, l3.next
            else:
                l3.next = ListNode(list2.val)
                list2, l3 = list2.next, l3.next

        if list1 or list2:
            l3.next = list1 if list1 else list2

        return l3_head.next


s = Solution()
list1 = ListNode(val=1)
list1.next = ListNode(val=2)
list1.next.next = ListNode(val=4)
list2 = ListNode(val=1)
list2.next = ListNode(val=3)
list2.next.next = ListNode(val=4)
print(s.mergeTwoLists(list1, list2))
