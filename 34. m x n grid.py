# m x n grid
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head

    # Calculate the length of the list
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Effective rotations
    k = k % length
    if k == 0:
        return head

    # Find the new tail (length - k - 1) and the new head (length - k)
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    tail.next = head

    return new_head
# Helper function to create a linked list from a list
def list_to_linkedlist(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
head = list_to_linkedlist([1, 2, 3, 4, 5])
k = 2
rotated_head = rotateRight(head, k)
print(linkedlist_to_list(rotated_head))  # Output: [4, 5, 1, 2, 3]

# Test Case 2
head = list_to_linkedlist([0, 1, 2])
k = 4
rotated_head = rotateRight(head, k)
print(linkedlist_to_list(rotated_head))  # Output: [2, 0, 1]
