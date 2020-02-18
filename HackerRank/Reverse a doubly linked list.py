def reverse(head):
    temp = head
    while temp:
        next = temp.next
        temp.next = temp.prev
        prev = temp
        temp = next

    head = prev
    return head
    
Link: https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
