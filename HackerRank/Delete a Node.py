def deleteNode(head, position):
    temp = head
    if position == 0:
        head = temp.next
        return head
    counter = 0
    prev = head
    while temp.next:
        if counter == position:
            prev.next = temp.next
            temp = None
            return head
        prev = temp
        temp = temp.next
        counter += 1
        
Link: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
