def reverse(head):
    current = head
    prev = None
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    head = prev
    return head
    
Link: Reverse a linked list
