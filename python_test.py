# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ''
        num2 = ''

        while l1:
            num1 = f"{l1.val}" + num1
            l1 = l1.next
            print(l1)

        while l2:
            num2 = f"{l2.val}" + num2
            l2 = l2.next
            print(l2)

        total_sum = str(int(num1) + int(num2))

        dummy_head = ListNode(0)
        current = dummy_head
        for digit in reversed(total_sum):
            current.next = ListNode(int(digit))
            current = current.next
        
        return dummy_head.next

def print_linked_list(head):
    """Helper function to print the linked list."""
    current = head
    while current:
        print(current.val, end=' -> ')
        current = current.next
    print('None')

def test_add_two_numbers():
    # Create first linked list: 342 (2 -> 4 -> 3)
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    # Create second linked list: 465 (5 -> 6 -> 4)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    # Expected result: 807 (7 -> 0 -> 8)
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    
    # Print result linked list
    print("Result linked list:")
    print_linked_list(result)

if __name__ == "__main__":
    test_add_two_numbers()
