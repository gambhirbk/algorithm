import random
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def shuffleList(self, head):
        if not self.head or not self.head.next:
            return head

        left = slow = fast = head 

        fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None

        left_sorted = shuffleList(left)
        right_sorted = shuffleList(right)


        return merge(left_sorted, right_sorted)

    def merge(self, l1, l2):
        dummy = ListNode(-1)
        prev = dummy
        flip = random.randint(l1.val, l2.val)
        while l1 or l2:
            if l1.val == flip:
                prev.next = l1
                l1 = l1.next
            else:
                prev_next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 or l2
        return dummy.next
