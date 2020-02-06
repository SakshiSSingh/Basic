
def insertNodeAtPosition(head, data, position):
    counter = 0
    temp = head
    while temp.next:
        if counter==position-1:
            current = SinglyLinkedListNode(data)
            current.next = temp.next
            temp.next = current
        temp = temp.next
        counter += 1
    return head


Link: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
